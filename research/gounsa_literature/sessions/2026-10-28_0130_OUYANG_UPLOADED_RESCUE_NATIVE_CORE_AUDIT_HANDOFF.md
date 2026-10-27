# 2026-10-28 Ouyang actual user ZIP source forensic audit — runbook

## User intent and current evidence
Recover ONE published 5–10cm forest canopy and true 2D rain+flow detachment deposition model using uploaded Ouyang source; repeated stream errors required continuation. In this session original Source_code.zip and Data.zip were available locally, extracted and inspected, and native gfortran compiles and unit tests performed.

## Source exact facts
Source_code.zip: 68 archive entries, 45 Fortran `.f90` + solver.dll/solver.lib + original input (grid829x1520,10m and LAI/landuse/etc). Data.zip:59 archive entries of rain-gauge and particle-size datasets. The **2023 original main actually calls** rain_model_InterceptionV; rain_model_Infiltration; comp_one_region; then original X/Y extra terms include model_deposition_JHE and model_erosion_JHE. This is more than just a matched DOI.
2023 solver.dll PE timestamp 2022-10-25, 486,912 bytes SHA256 5019d1b4ccaa538a26c517fab155eed6d4d4bf5cd95a6b2eb43e867c9fb8bed1. Exports9 including COMP_ONE_REGION and COMP_FBX/FY, imports 5 symbols from massflow.exe plus fmpich2 and libiomp5md. No original COMP_ONE_REGION Fortran in user-provided ZIP, no massflow.exe either. Win Intel Fortran/MPICH2 linkage missing. DLL original code not truly publicly provided.

## Compiler and native numerical outcomes
GNU Fortran14.2 compiled **40 of 45 untouched .f90** to object; 4 blocked only missing mpif.h, one blocked Intel-only inquire(directory) extension (pre_dir_filename). All compiled separately, NOT linked to an executable. Synthetic native call original model_deposition_JHE on three artificial water-depth and sediment-concentration states: h.05,Cv.20 zero, h.15,Cv.05 zero, h.15,Cv.20 4.94478e-4m/s. Original code explicitly sets all grain deposition to zero if h<0.1m OR Cv<0.1. Original erosion sets zero if h<0.01m. Shallow sparse sediment hillslope storm concern. Original separate X/Y uses n_v=829 as orientation test, unsafe resized meshes. Other dry division, canopy splash constant and cap mismatch flagged, unvalidated as whole run.

## Discovery: 2018 original ZIP code comparison is DONE, not pending
Research group https://github.com/anhuicong323/Ouyang_2018 links four public ZIPs. A GitHub Actions workflow `.github/workflows/gounsa_ouyang2018_massflow_original_solver_source_audit.yml` fetched & inspected all four archives without executing the code, stored permanent 2018 archive manifest at `research/gounsa_literature/sessions/2026-10-28_OUYANG2018_MASSFLOW_ARCHIVE_MACHINE_MANIFEST.json` (Github bot). Exact 2018 legacy massflow.zip 43 files; solver.dll 622592B, erosion_JHE 968B, deposition_JHE1049B, NO 2023 canopy file nor COMP_ONE_REGION Fortran source. 2018 example has old massflow.exe 1,027,584B which cannot be advertised compatible to 2023 DLL without matching exports/ABI. 2018 DLL swap is NO-GO.

## Outputs and durable archive
One local source report `/mnt/data/oy_recovery/GOUNSA_OUYANG_20261028_NATIVE_SOURCE_AUDIT.md`; original routine test `test_deposition_original.f90` and reproducibility bundle `/mnt/data/oy_recovery/GOUNSA_OUYANG_20261028_REPRODUCIBILITY.zip`. Link only if container path verified. GitHub decision [2026-10-28_OUYANG_2023_UPLOADED_FORTRAN_NATIVE_COMPILE_SEDIMENT_SHALLOW_GATE_AND_2018_DLL_MISMATCH.md](../decisions/2026-10-28_OUYANG_2023_UPLOADED_FORTRAN_NATIVE_COMPILE_SEDIMENT_SHALLOW_GATE_AND_2018_DLL_MISMATCH.md), original model canonical update `models/Ouyang_2023_Postfire_LAI_2D_HR.md`, MASTER updated.

## Next viable steps (not accomplished)
1. Obtain 2022/2023 exact Intel-compatible massflow.exe + solver.dll matching original and fmpich2.dll under Windows x64, OR exact Fortran source for COMP_ONE_REGION, including numerical integrators COMP_FBX/FY. No source has yet been found; cannot claim full build.
2. Native 10m as-published reproducer first: validate rain, canopy, infiltration, HR sediment, mass budget, local bed; compare actual published outputs.
3. If changing code for 5–10cm, replace hardcoded n_v indexing with explicit axis, investigate h/cv gates, dry-cell divisions, finite topsoil and bed flux closure; re-run dx/dt convergence. This creates scientifically NEW verified derived version, not original 2023 study unchanged.
4. Miscanthus and oak have different LAI/storage/drip KE, root/litter/rock structure. Existing 2023 Aston canopy only; no native leaf-drop KE or stemflow confirmed; avoid overclaim.
