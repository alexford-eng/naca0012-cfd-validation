# NACA 0012 CFD Validation Study

This project has been independently carried out by a second year Mechanical Engineering student studying at the University of Bath and is a validation study of 2D RANS CFD for the NACA 0012 aerofoil benchmarked against NASA Turbulence Modelling Resource data from seven independent CFD codes.

---

## Status of project phases

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Reference baselines — XFOIL panel method, analytical theory, published experimental data | Complete |
| 1 | 2D RANS CFD of NACA 0012 in OpenFOAM, with mesh independence and convergence study | Complete |
| 1.5| Angle sweep at alpha = 10 degrees and 15° on the validated grid | Complete |

---

## Why validation-first

Since CFD returns an answer regardless of whether the setup is correct, a validation first approach was taken. Confirming that acquired results are trustworthy is much more meaningful than simply producing results, hence the importance of comparison to known data (which is why the NACA 0012 was chosen specifically). Only after reproducing an accepted finding should the method be applied elsewhere.

---

## Headline Results

The XFOIL lift slope was found to be within 1.0% of thin aerofoil theory.                                The mesh independence study was done across 4 refinement levels from 3,584 cells to 229,376 cells, and an order of convergence of 2.46 was found.                                                                  Drag error reduced from +98% to +3.9% from the least to most refined mesh, with the two finest grids being only 0.3% different. The 3.9% difference is localised to the leadig edge skin friction resolution, and the spread among the reference codes is 2.2%.                                                                                     Surface pressure distribution matches CFL3D reference almost exactly, and skin friction matches in shape with a minor discrepancy at the leading-edge. Lift agreed with NASA benchmark data to within 1% across α = 0°, 10° and 15°, matching the precision level the seven reference codes achieve among themselves.
