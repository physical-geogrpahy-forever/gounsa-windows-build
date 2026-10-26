"""Gounsa standalone canopy PROTOTYPE (not SWEHR native or calibrated).

Independent coefficients are necessary for site-specific LAI capacity and gaps.
"""
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class CanopyParams:
    smax_per_lai_m: float
    k_gap: float
    drain_k_m_s: float
    drain_g_inv_m: float
    stem_frac_of_drain: float = 0.0

def canopy_step(lai, storage_m, gross_rain_m_s, dt_s, params: CanopyParams):
    """Implicit drainage, 2D arrays. All rates m/s and stored water m."""
    lai, c0, p = np.broadcast_arrays(
        np.asarray(lai, dtype=float),
        np.asarray(storage_m, dtype=float),
        np.asarray(gross_rain_m_s, dtype=float))
    ps = [params.smax_per_lai_m, params.k_gap, params.drain_k_m_s,
          params.drain_g_inv_m, params.stem_frac_of_drain]
    if (dt_s <= 0 or not np.isfinite(dt_s) or
            not np.all(np.isfinite(ps)) or min(ps) < 0 or
            params.stem_frac_of_drain > 1 or
            np.any(~np.isfinite(lai + c0 + p)) or
            np.any(lai < 0) or np.any(c0 < 0) or np.any(p < 0)):
        raise ValueError("nonfinite, negative or invalid input")
    s = params.smax_per_lai_m * lai
    direct_fraction = np.exp(-params.k_gap * lai)
    direct = p * direct_fraction
    available = c0 + (p-direct)*dt_s
    active = s > 0
    lo = np.zeros_like(available)
    hi = available.copy()
    for _ in range(60):
        mid = 0.5 * (lo+hi)
        drain = np.where(active, params.drain_k_m_s *
            np.exp(np.clip(params.drain_g_inv_m*(mid-s),-80,80)),0.0)
        mask = (mid + dt_s*drain > available) & active
        hi = np.where(mask,mid,hi)
        lo = np.where(~mask & active,mid,lo)
    c1 = np.where(active, (lo+hi)*0.5,0.0)
    out = np.maximum(available-c1,0.0)/dt_s
    stem = out * params.stem_frac_of_drain
    drip = out-stem
    closure = p*dt_s+c0-(direct+drip+stem)*dt_s-c1
    return dict(storage_m=c1,direct_m_s=direct,drip_m_s=drip,
                stem_m_s=stem,closure_m=closure,
                throughfall_fraction=direct_fraction,capacity_m=s)

def event_run(lai, rain_rates_m_s, dt_s, params, initial_storage_m=None):
    """Aggregate event canopy water ledger on a raster; keep final storage."""
    lai = np.asarray(lai,dtype=float)
    c = (np.zeros_like(lai) if initial_storage_m is None else
         np.broadcast_to(initial_storage_m,lai.shape).copy())
    c_init=c.copy()
    depth = dict(gross_m=np.zeros_like(lai),
                 direct_m=np.zeros_like(lai),
                 drip_m=np.zeros_like(lai),
                 stem_m=np.zeros_like(lai))
    for rate in rain_rates_m_s:
        r=canopy_step(lai,c,rate,dt_s,params)
        depth['gross_m'] += np.broadcast_to(rate,lai.shape)*dt_s
        for k in ['direct','drip','stem']:
            depth[k+'_m'] += r[k+'_m_s']*dt_s
        c=r['storage_m']
    depth['storage_change_m']=c-c_init
    depth['closure_m']=(depth['gross_m']-depth['direct_m']-
        depth['drip_m']-depth['stem_m']-depth['storage_change_m'])
    return depth
