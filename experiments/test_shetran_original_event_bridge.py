#!/usr/bin/env python3
"""Contract tests of EXTERNAL postprocessor only; NOT an original native SHETRAN run."""
import csv
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from shetran_original_event_bridge import run, read_frd, encode_g7

class OriginalBoundaryBridgeTests(unittest.TestCase):
    def create_case(self, root):
        root=Path(root)
        frd=root/"case_frd.txt"
        frd.write_text(
            "COBRES synthetic unit-test\nGRID SQUARES IN X,Y DIRECTIONS\n"
            "      2      2      0\nGROUND SURFACE ELEVATION\n"
            "      2\n 10.000  9.000\n"
            "      1\n  8.000  7.000\nNEXT INPUT HEADER\n"
        )
        def grid(name,col,vals):
            f=root/name
            with f.open("w",newline="") as fd:
                w=csv.writer(fd);w.writerow(["iy","ix",col])
                for key,v in vals.items():w.writerow([*key,v])
            return str(f)
        keys=[(1,1),(1,2),(2,1),(2,2)]
        one={(iy,ix):v for (iy,ix),v in zip(keys,[0.0,2.0,2.0,2.0])}
        ends={(iy,ix):v for (iy,ix),v in zip(keys,[0.0,7.0,7.0,7.0])}
        depth={(iy,ix):.20 for iy,ix in keys}
        rate=root/"rate.csv"
        with rate.open("w",newline="") as fd:
            w=csv.writer(fd);w.writerow(["time_s","iy","ix","rate_mm_day"])
            for t in [0,3600]:
                for iy,ix in keys:w.writerow([t,iy,ix,240 if (iy,ix)==(2,1) else 0])
        return SimpleNamespace(frd=str(frd),erosion_rate_csv=str(rate),
            soil_depth_csv=grid("soil.csv","depth_m",depth),
            loose_initial_csv=grid("before.csv","s_t_dp_mm",one),
            loose_final_csv=grid("after.csv","s_t_dp_mm",ends),
            event_seconds=3600.,max_rounding_m=.00001,output_dir=str(root/"result"))

    def test_physical_change_and_original_frd_roundtrip(self):
        with tempfile.TemporaryDirectory() as folder:
            args=self.create_case(folder)
            d=run(args)
            self.assertFalse(d["restart_ready"])
            _,_,_,nx,ny,z=read_frd(Path(args.output_dir,"input_next_frd.txt").read_text())
            self.assertEqual((nx,ny),(2,2))
            self.assertAlmostEqual(z[2,1],9.995,places=6) # 10mm gross soil - 5mm deposition
            self.assertAlmostEqual(z[2,2],9.005,places=6) # only 5mm deposition
            self.assertAlmostEqual(z[1,1],8.0,places=6)
            with Path(args.output_dir,"next_soil_depth.csv").open() as handle:
                q=list(csv.DictReader(handle))
            self.assertAlmostEqual(float(next(x["depth_m"] for x in q
                if x["iy"]=="2" and x["ix"]=="1")),.19,places=6)
            self.assertAlmostEqual(d["max_native_F7_rounding_m"],0,places=9)
            info=json.loads(Path(args.output_dir,"QA_AND_RESTART_BLOCKERS.json").read_text())
            self.assertIn("SY52 FBETA particle-size composition per cell at end of storm",
                          info["blocking_missing_initial_states"])
    def test_original_native_frd_encoding_precision_guard(self):
        with self.assertRaises(ValueError):
            encode_g7(650.00012,1e-5)  # G7.0 cannot silently truncate <1mm changes.
    def test_event_duration_must_match_rate_samples(self):
        with tempfile.TemporaryDirectory() as folder:
            args=self.create_case(folder)
            args.event_seconds=7200
            with self.assertRaisesRegex(ValueError,"must have endpoints"):
                run(args)
    def test_impossible_erosion_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            args=self.create_case(folder)
            with open(args.erosion_rate_csv,"w",newline="") as f:
                w=csv.writer(f);w.writerow(["time_s","iy","ix","rate_mm_day"])
                for t in [0,3600]:
                    for iy in [1,2]:
                        for ix in [1,2]:w.writerow([t,iy,ix,24000])
            with self.assertRaisesRegex(ValueError,"exceeds initial depth"):
                run(args)
if __name__=="__main__":unittest.main(verbosity=2)
