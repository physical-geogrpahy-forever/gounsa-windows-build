import unittest
import numpy as np
try:
    from canopy_event import CanopyParams,canopy_step,event_run
except ModuleNotFoundError:
    from experiments.gounsa_deadline_20261027.canopy_event import CanopyParams,canopy_step,event_run

PARAMS=CanopyParams(.0008,.5,5e-8,3900)
class TestCanopyWater(unittest.TestCase):
    def test_zero_lai(self):
        r=canopy_step(np.zeros((3,3)),0.,30e-3/3600,60,PARAMS)
        self.assertLess(float(np.max(np.abs(r['direct_m_s']-30e-3/3600))),1e-15)
        self.assertEqual(float(np.max(r['storage_m'])),0.)
        self.assertEqual(float(np.max(r['drip_m_s'])),0.)
    def test_heterogeneous_1hr(self):
        r=event_run(np.array([[0.,.5,2.],[1.,4.,8.]]),[30e-3/3600]*60,60,PARAMS)
        self.assertLess(float(np.max(np.abs(r['closure_m']))),1e-12)
        self.assertGreater(float(r['storage_change_m'][1,2]),0.)
        self.assertLess(float(r['direct_m'][1,2]),float(r['direct_m'][0,0]))
    def test_dry_drainage(self):
        r=event_run(np.array([[3.]]),[30e-3/3600]*60+[0.]*120,60,PARAMS)
        self.assertLess(float(np.max(np.abs(r['closure_m']))),1e-12)
        self.assertGreater(float(r['drip_m'][0,0]),0.)
    def test_stemflow_is_partition_not_extra(self):
        p=CanopyParams(.0008,.5,5e-8,3900,.25)
        r=event_run(np.array([[2.]]),[30e-3/3600]*60,60,p)
        self.assertLess(float(np.max(np.abs(r['closure_m']))),1e-12)
        f=r['stem_m'][0,0]/(r['drip_m'][0,0]+r['stem_m'][0,0])
        self.assertAlmostEqual(float(f),.25)
    def test_five_intensities_plus_dry(self):
        for mmh in [0,10,20,30,40,50]:
            r=event_run(np.array([[.2,2,4.]]),[mmh*1e-3/3600]*60,60,PARAMS)
            self.assertLess(float(np.max(np.abs(r['closure_m']))),1e-12)
    def test_invalid(self):
        with self.assertRaises(ValueError): canopy_step(2,-1,0.,60,PARAMS)
        with self.assertRaises(ValueError): canopy_step(2,0.,-1.,60,PARAMS)
        with self.assertRaises(ValueError): canopy_step(2,0.,1.,0,PARAMS)
if __name__ == '__main__':
    unittest.main()
