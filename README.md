# Gounsa Windows LPJ-GUESS build

This repository builds the Gounsa-patched LPJ-GUESS 4.1.1 Windows command-line executable.

The workflow intentionally does **not** store or modify the upstream LPJ-GUESS archive in GitHub. Instead it downloads the official Zenodo `guess_4.1.1.zip`, requires SHA-256 `9d30881c180bd2d291fea0a5d7e7cf22fc33512bf4c99b452722d4d8d3d8f193`, applies `GOUNSA_LPJ411_REBASE_v0_38.patch`, and builds `guesscmd.exe` with MSVC and NetCDF C supplied by vcpkg.

The resulting artifact is named `gounsa-lpjguess411-windows-x64-native` and contains `bin/guesscmd.exe` plus the app-local vcpkg runtime DLLs.

Scientific note: obtaining a Windows binary changes only the platform packaging. It does not upgrade the current Gounsa geomorphology from literature-transfer sensitivity to site-calibrated prediction, and it does not by itself add geomorph-to-LPJ hydraulic feedback.
