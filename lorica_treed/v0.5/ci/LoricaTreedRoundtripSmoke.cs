using System;
using System.IO;
using System.Linq;
using System.Reflection;
using LORICA4;

public static class LoricaTreedRoundtripSmoke
{
    static readonly BindingFlags BF = BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public;

    static FieldInfo Field(object o, string name)
    {
        var f = o.GetType().GetField(name, BF);
        if (f == null) throw new MissingFieldException(o.GetType().FullName, name);
        return f;
    }

    static T Get<T>(object o, string name) => (T)Field(o, name).GetValue(o);
    static void Set(object o, string name, object value) => Field(o, name).SetValue(o, value);

    static MethodInfo Method(object o, string name)
    {
        var m = o.GetType().GetMethod(name, BF);
        if (m == null) throw new MissingMethodException(o.GetType().FullName, name);
        return m;
    }

    static void Main(string[] args)
    {
        if (args.Length != 2)
        {
            Console.Error.WriteLine("Usage: LoricaTreedRoundtripSmoke.exe COUPLING_DIR WORK_DIR");
            Environment.Exit(2);
        }

        string couplingDir = Path.GetFullPath(args[0]);
        string workDir = Path.GetFullPath(args[1]);
        Directory.CreateDirectory(workDir);
        Environment.SetEnvironmentVariable("LORICA_TREED_COUPLING_DIR", couplingDir);

        using (var form = new Mother_form())
        {
            const int nr = 2, nc = 2;
            const int nodata = -9999;

            Set(form, "nr", nr);
            Set(form, "nc", nc);
            Set(form, "nodata_value", nodata);
            Set(form, "run_number", 9001);
            Set(form, "t", 0);
            Set(form, "workdir", workDir);
            Set(form, "max_soil_layers", 1);

            var inputheader = Get<string[]>(form, "inputheader");
            inputheader[0] = "ncols         2";
            inputheader[1] = "nrows         2";
            inputheader[2] = "xllcorner     0";
            inputheader[3] = "yllcorner     0";
            inputheader[4] = "cellsize      10";
            inputheader[5] = "NODATA_value  -9999";

            var dtm = new double[,] { { 100.0, 99.0 }, { 98.0, 97.0 } };
            var soildepth = new double[,] { { 1.0, 1.0 }, { 1.0, 1.0 } };
            Set(form, "dtm", dtm);
            Set(form, "soildepth_m", soildepth);
            Set(form, "veg_correction_factor", new double[nr, nc]);
            Set(form, "root_cohesion_kPa_new", new double[nr, nc]);

            var layer = new double[nr, nc, 1];
            var texture = new double[nr, nc, 1, 5];
            var young = new double[nr, nc, 1];
            var old = new double[nr, nc, 1];
            for (int r = 0; r < nr; r++)
            for (int c = 0; c < nc; c++)
            {
                layer[r, c, 0] = 1.0;
                texture[r, c, 0, 1] = 400.0; // sand kg
                texture[r, c, 0, 2] = 400.0; // silt kg
                texture[r, c, 0, 3] = 200.0; // clay kg
                texture[r, c, 0, 4] = 0.0;
                young[r, c, 0] = 10.0;
                old[r, c, 0] = 10.0;
            }
            Set(form, "layerthickness_m", layer);
            Set(form, "texture_kg", texture);
            Set(form, "young_SOM_kg", young);
            Set(form, "old_SOM_kg", old);

            var py = Get<double[]>(form, "Py");
            var tavgy = Get<int[]>(form, "Tavgy");
            var tminy = Get<int[]>(form, "Tminy");
            var tmaxy = Get<int[]>(form, "Tmaxy");
            var dy = Get<int[]>(form, "Dy");
            for (int d = 0; d < 365; d++)
            {
                py[d] = 0.003; // 3 mm/day; already metres/day as expected after preparation
                tavgy[d] = 15;
                tminy[d] = 10;
                tmaxy[d] = 20;
                dy[d] = 4;
            }
            Set(form, "daily_weather_prepared_for_timestep", true);

            Method(form, "run_treed_coupling").Invoke(form, null);

            var rootCoh = Get<double[,]>(form, "root_cohesion_kPa_new");
            var cover = Get<double[,]>(form, "aridity_vegetation");
            var et = Get<double[,]>(form, "veg_correction_factor");

            double minCoh = double.PositiveInfinity, maxCoh = double.NegativeInfinity;
            double minCover = double.PositiveInfinity, maxCover = double.NegativeInfinity;
            for (int r = 0; r < nr; r++)
            for (int c = 0; c < nc; c++)
            {
                if (double.IsNaN(rootCoh[r,c]) || double.IsInfinity(rootCoh[r,c]) || rootCoh[r,c] <= 0)
                    throw new Exception("Invalid/non-positive Hwang root cohesion returned to LORICA.");
                if (double.IsNaN(cover[r,c]) || cover[r,c] < 0 || cover[r,c] > 1)
                    throw new Exception("Invalid TREED FPC returned to LORICA.");
                if (double.IsNaN(et[r,c]) || et[r,c] < 0.85 - 1e-9 || et[r,c] > 1.0 + 1e-9)
                    throw new Exception("Invalid TREED-derived LORICA ET multiplier.");
                minCoh = Math.Min(minCoh, rootCoh[r,c]);
                maxCoh = Math.Max(maxCoh, rootCoh[r,c]);
                minCover = Math.Min(minCover, cover[r,c]);
                maxCover = Math.Max(maxCover, cover[r,c]);
            }

            string outDir = Path.Combine(workDir, "TREED_exchange_run_9001", "0001", "output");
            string[] required = {
                "treed_rootC_areanorm_gC_m2.asc",
                "treed_r_s_r.asc",
                "treed_rootcohesion_Hwang2015_raw_kPa.asc",
                "treed_rootcohesion_Hwang2015_kPa.asc",
                "treed_rootcohesion_summary.csv"
            };
            foreach (var name in required)
                if (!File.Exists(Path.Combine(outDir, name)))
                    throw new FileNotFoundException("Missing roundtrip output", Path.Combine(outDir, name));

            string marker = Path.Combine(workDir, "LORICA_TREED_ROUNDTRIP_OK.txt");
            File.WriteAllText(marker,
                "LORICA_CSHARP_TO_JULIA_TO_CSHARP=PASS" + Environment.NewLine +
                "root_cohesion_min_kPa=" + minCoh.ToString("R") + Environment.NewLine +
                "root_cohesion_max_kPa=" + maxCoh.ToString("R") + Environment.NewLine +
                "FPC_min=" + minCover.ToString("R") + Environment.NewLine +
                "FPC_max=" + maxCover.ToString("R") + Environment.NewLine);
            Console.WriteLine(File.ReadAllText(marker));
        }
    }
}
