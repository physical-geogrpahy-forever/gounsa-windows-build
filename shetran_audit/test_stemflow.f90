program stemflow_test
  use, intrinsic :: iso_fortran_env, only: real64
  use stemflow_spatial_core, only: partition_stemflow
  implicit none
  real(real64) :: area(3), cap(3), store(3), p(3), d(3), stem(3), local(3), resid
  real(real64) :: max_store(3), rate(3), infiltration_area(3), dt
  integer :: target(3)
  dt=60._real64
  area=[1._real64,1._real64,1._real64]
  target=[1,3,3]
  cap=[0.4_real64,0.4_real64,0._real64]
  max_store=0._real64
  rate=2._real64
  infiltration_area=[0.40_real64,0.02_real64,1._real64]
  p=[20._real64,20._real64,20._real64]/3600000._real64
  d=[4._real64,4._real64,0._real64]/3600000._real64
  store=0._real64
  call partition_stemflow(3,dt,area,target,cap,max_store,rate,infiltration_area,p,d,store,stem,local,resid)
  if(abs(resid)>1e-12_real64) error stop 'TEST WATER CLOSURE FAILED'
  if(abs(local(1)*3600000._real64-4._real64)>1e-7_real64) error stop 'GRASS LOCAL INTENSITY FAILED'
  if(abs(local(2)*3600000._real64-80._real64)>1e-7_real64) error stop 'OAK LOCAL INTENSITY FAILED'
  if(abs(sum(p*area)*dt-3*20._real64/3600000._real64*dt)>1e-9_real64) &
     error stop 'MASS TRANSFER FAILED'
  print '(A,ES14.6)', 'stemflow volume closure m3=',resid
  print '(A,F10.4)', 'grass near-culm intensity mm/h=',local(1)*3600000._real64
  print '(A,F10.4)', 'oak near-stem intensity mm/h=',local(2)*3600000._real64
  print '(A,F10.4)', 'stem-receiving grid intensity mm/h=',stem(3)*3600000._real64
  print '(A)', 'PASS STEMFLOW PARTITION UNIT TEST'
  cap(1)=1._real64
  rate(1)=0.01_real64
  max_store(1)=.0005_real64
  p=0._real64
  d=0._real64
  store(1)=.0002_real64
  store(2:3)=0._real64
  call partition_stemflow(3,dt,area,target,cap,max_store,rate,infiltration_area,p,d,store,stem,local,resid)
  if (abs(resid)>1e-12_real64) error stop 'DRAINAGE MASS ERROR'
  if(store(1)<=0._real64 .or. stem(1)<=0._real64) error stop 'NO DELAYED DRAINAGE'
  print '(A)', 'PASS DELAYED TRUNK DRAINAGE UNIT TEST'
end program stemflow_test
