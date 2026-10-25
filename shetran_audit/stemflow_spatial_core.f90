! Research-only proposed SHETRAN in-model stemflow routing core.
! Water routing/mass conservation UNIT TESTED, NOT integrated into the
! official SHETRAN executable. Subgrid infiltration is NOT solved.
module stemflow_spatial_core
  use, intrinsic :: iso_fortran_env, only: real64
  implicit none
  private
  public :: partition_stemflow
contains
  subroutine partition_stemflow(n, dt_s, cellarea_m2, dest, capfrac, trunk_cap_m, &
                                 trunk_rate_per_s, infiltration_area_m2, pnet_mps, &
                                 drip_mps, store_m, stemrain_mps, local_intensity_mps, residual_m3)
    integer, intent(in) :: n, dest(n)
    real(real64), intent(in) :: dt_s, cellarea_m2(n), capfrac(n), trunk_cap_m(n), &
                               trunk_rate_per_s(n), infiltration_area_m2(n)
    real(real64), intent(inout) :: pnet_mps(n), drip_mps(n), store_m(n)
    real(real64), intent(out) :: stemrain_mps(n), local_intensity_mps(n), residual_m3
    real(real64) :: water_before, storage_before, water_after, storage_after
    real(real64) :: capture_rate, available_m, released_m, q_m3s, release_fraction, overflow_m
    integer :: i, j
    if (n<1 .or. dt_s<=0._real64) error stop 'invalid size/dt'
    if (any(cellarea_m2<=0._real64) .or. any(infiltration_area_m2<=0._real64)) error stop 'invalid area'
    if (any(dest<1) .or. any(dest>n)) error stop 'invalid receiving cell'
    if (any(capfrac<0._real64) .or. any(capfrac>1._real64)) error stop 'invalid capture fraction'
    if (any(trunk_cap_m<0._real64) .or. any(trunk_rate_per_s<0._real64)) error stop 'negative trunk parameter'
    if (any(pnet_mps<-1e-15_real64) .or. any(drip_mps<-1e-15_real64)) error stop 'negative rain'
    if (any(drip_mps>pnet_mps+1e-12_real64)) error stop 'drip exceeds total ground input'
    if (any(store_m<-1e-15_real64)) error stop 'negative trunk storage'
    water_before=sum(pnet_mps*cellarea_m2)*dt_s
    storage_before=sum(store_m*cellarea_m2)
    stemrain_mps=0._real64
    local_intensity_mps=0._real64
    do i=1,n
       ! Morphological capture fraction is provisionally parameterised;
       ! it must be derived and validated for each vegetation type.
       capture_rate=capfrac(i)*drip_mps(i)
       pnet_mps(i)=pnet_mps(i)-capture_rate
       drip_mps(i)=drip_mps(i)-capture_rate
       available_m=store_m(i)+capture_rate*dt_s
       release_fraction=1._real64-exp(-trunk_rate_per_s(i)*dt_s)
       released_m=available_m*release_fraction
       overflow_m=max(0._real64,available_m-released_m-trunk_cap_m(i))
       released_m=released_m+overflow_m
       store_m(i)=available_m-released_m
       j=dest(i)
       q_m3s=released_m*cellarea_m2(i)/dt_s
       stemrain_mps(j)=stemrain_mps(j)+q_m3s/cellarea_m2(j)
       ! Diagnostic only! The receiver soil uses cell-average pnet,
       ! not this locally concentrated intensity, until VS is modified.
       local_intensity_mps(i)=q_m3s/infiltration_area_m2(i)
    end do
    pnet_mps=pnet_mps+stemrain_mps
    water_after=sum(pnet_mps*cellarea_m2)*dt_s
    storage_after=sum(store_m*cellarea_m2)
    residual_m3=water_before+storage_before-water_after-storage_after
    if (abs(residual_m3)>1e-10_real64*max(1._real64,water_before+storage_before)) &
        error stop 'stemflow water-volume closure failed'
    if (any(pnet_mps<-1e-12_real64)) error stop 'negative net rainfall'
  end subroutine partition_stemflow
end module stemflow_spatial_core
