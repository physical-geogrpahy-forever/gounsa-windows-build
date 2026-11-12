# LORICA–TREED v0.6: root-cohesion audit

v0.6 does **not** add a new geomorphic or vegetation process. It keeps the validated v0.5 coupling engine and audits the numerical consequence of converting TREED root biomass to LORICA root cohesion with Hwang et al. (2015), Eq. (5):

`Cr = K * Tr * Br / rho_r`

## Why this audit was added

The successful v0.5 C# → Julia → C# roundtrip produced approximately 1.8–1.9 kg C m⁻² of area-normalized TREED root carbon (about 3.9–4.0 kg dry root biomass m⁻²). This biomass is not outside the field range reported by Hwang et al. (2015), whose soil pits contained roughly 0.31–5.24 kg m⁻² belowground biomass.

The problem is the tensile-strength parameter used during landslide calculation. The v0.5 diagnostic default used Korean mean root tensile strength (about 15–22 MPa). Hwang et al. instead found their best landslide prediction when spatially varying root biomass was combined with the **weakest, near-saturated root tensile strength**. Hwang also reported that the spatially uniform 21.6 kPa Wu-method cohesion case was already too strong and produced no predicted landslides.

Therefore v0.6 separates:

1. TREED root biomass,
2. ordinary measured mean root tensile strength,
3. storm/wet-root weakening,
4. Wu-model reduction relative to direct shear,
5. the effective event-scale tensile strength implied by an external cohesion benchmark.

No inferred value becomes a model default automatically.

## Literature anchors used

- Hwang et al. (2015), JGR Biogeosciences, DOI 10.1002/2014JG002824.
- Hales et al. (2009), JGR Earth Surface, DOI 10.1029/2008JF001168: vertically integrated mean root cohesion across Coweeta pits was 7.6 ± 5.4 kPa with the Wu method and 3.4 ± 2.4 kPa with the Fiber Bundle Model (FBM); Wu values ranged 3.4–22.4 kPa.
- Hales & Miniat (2017), Earth Surface Processes and Landforms, DOI 10.1002/esp.4039: laboratory roots showed a 40% strength decline from 20–40% to 80–100% root moisture.
- Kim et al. (KSFE-FETEC 2025), *Evaluating Soil Reinforcement by Lateral Root Systems of Major Tree Species in South Korea*: average tensile strength 15.9 MPa for Pinus densiflora; Wu-model cohesion was 1.5–5.1 times direct-shear values; reduction-corrected root cohesion was 9.0 kPa for P. densiflora, 9.1 for P. koraiensis, 4.3 for L. kaempferi, and 12.9 for Q. mongolica.

## Interpretation

The audit reports the effective `Tr` required for Hwang Eq. (5) to reproduce each literature cohesion benchmark at the TREED biomass produced by the CI smoke simulation. This is a diagnostic inverse calculation, **not a claim that the inferred value was directly measured**.

The production model should not use the former 15–22 MPa mean tensile-strength profiles as landslide-event defaults until a wet/saturated Korean calibration is available.

## Additional Coweeta benchmark

The audit now also inverse-solves Hwang Eq. (5) for the Hales et al. (2009) Coweeta means (7.6 kPa Wu; 3.4 kPa FBM). These are independent field-derived reinforcement benchmarks from the same general southern Appalachian literature lineage that Hwang et al. later used. They are audit targets only and do not become hidden defaults.
