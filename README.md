# NACA 0012 CFD Validation Study

Note: Full write-up in progress. Phase 0 complete; Phase 1 (OpenFOAM RANS) currently in progress.

A 2D aerodynamic study of the NACA 0012 aerofoil, built validation-first: every result is
benchmarked against an independent method or published data before the method is extended to
new geometry.

**Author:** Alex Ford — MEng Mechanical Engineering, University of Bath
**Status:** In progress. Phase 0 complete.

---

## Why validation-first

CFD always returns an answer. It does not warn you when the mesh is too coarse, the domain too
small, or the turbulence model inappropriate — it returns plausible-looking numbers regardless.
The value of a simulation therefore lies not in producing a result but in demonstrating that the
result is trustworthy.

This project is structured around that principle. The starting geometry is deliberately
unglamorous: the NACA 0012 is the most extensively measured aerofoil in existence, so a correct
answer is known in advance. Only once the method reproduces that known answer is it applied to
geometry where no reference data exists.

---

## Project phases

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Reference baselines — XFOIL panel method, analytical theory, published experimental data | Complete |
| 1 | 2D RANS CFD of NACA 0012 in OpenFOAM, with mesh independence and convergence study | Not started |
| 2 | Inverted wing in ground effect — downforce and drag across ride heights | Not started |
| 3 | Multi-element wing, gap and overlap sweep | Stretch goal |

---

## Phase 0 — XFOIL baseline

### Conditions

| Parameter | Value |
|-----------|-------|
| Software | XFLR5 v6.62 (XFOIL panel method with integral boundary layer) |
| Aerofoil | NACA 0012, 160 panels |
| Polar type | Type 1 (fixed speed) |
| Reynolds number | 6.0 x 10^6 |
| Mach number | 0.00 (incompressible) |
| NCrit | 9.0 (free transition, e^N method) |
| Forced transition | None (x/c = 1.00 top and bottom) |
| Angle of attack | 0 deg to 15 deg, 0.5 deg increments |
| Converged points | 31 of 31 |

### Results

| Quantity | Value |
|----------|-------|
| Lift curve slope, alpha = 0–8 deg | 0.1108 per degree |
| Thin aerofoil theory (2*pi per radian) | 0.10966 per degree |
| Difference from theory | +1.0% |
| Cl at alpha = 5 deg | 0.5603 |
| Cd at alpha = 0 deg | 0.00507 |
| Upper surface transition at alpha = 0 | x/c = 0.4119 |
| Lower surface transition at alpha = 0 | x/c = 0.4119 |

### Validation checks

**Zero lift at zero incidence.** Cl = 0.0000 and Cm = 0.0000 at alpha = 0. A symmetric section
must produce no net force at zero incidence; any deviation would indicate a geometry or setup
error.

**Symmetric transition at zero incidence.** Upper and lower surface transition locations agree to
four decimal places (x/c = 0.4119). The flow field is symmetric, as the geometry requires.

**Opposing transition trends with incidence.** As alpha increases, upper surface transition moves
forward (x/c = 0.41 to 0.008 at 15 deg) while lower surface transition moves aft (x/c = 0.41 to
1.00). This reflects the strengthening adverse pressure gradient on the suction side and the
increasingly favourable gradient on the pressure side.

**Lift slope against analytical theory.** The fitted slope exceeds thin aerofoil theory by 1.0%.
This is the expected direction and magnitude: finite thickness raises the lift slope, while
boundary layer displacement reduces it through effective decambering. At Re = 6 x 10^6 the
boundary layer is thin and the thickness effect dominates marginally. Both effects are visible in
the data — the local slope is 0.113 per degree between 0 and 1 deg, falling to 0.105 per degree
between 7.5 and 8 deg as the boundary layer thickens.

**Centre of pressure.** XCp remains between x/c = 0.238 and 0.247 across the sweep, consistent with
the quarter-chord aerodynamic centre expected for a symmetric section in attached flow.

---

## Known limitations

These are stated explicitly rather than left for a reader to find.

**XFOIL is not CFD.** It couples a panel method for the inviscid outer flow to an integral
boundary layer formulation. It is reliable in attached flow and degrades as separation develops.
It is used here as an independent cross-check, not as the primary result.

**Mach number mismatch with the reference experiment.** This baseline is run incompressible
(M = 0.00). The NASA Turbulence Modeling Resource validation case is at M = 0.15. The
Prandtl-Glauert correction implies a lift difference of order 1%, which is not negligible at the
level of agreement being claimed. This is accounted for explicitly in the comparison rather than
ignored.

**Drag is not directly comparable to tripped experimental data.** XFOIL predicts natural
transition at 41% chord, implying a substantial laminar run and correspondingly low skin friction.
Wind tunnel validation cases at this Reynolds number are frequently tripped near the leading edge.
Comparing free-transition and tripped drag coefficients is not a like-for-like comparison. The
Phase 1 RANS model uses Spalart-Allmaras, which runs fully turbulent by default, and will
therefore be comparable to tripped data but not to this baseline.

**No stall data.** The sweep terminates at 15 deg, below the stall angle at this Reynolds number.
XFOIL is least reliable near and beyond stall, so the sweep is deliberately confined to the
attached-flow region where the method is trustworthy.

---

## Repository structure

```
data/
  raw/          Unmodified solver output. Never edited.
  processed/    Cleaned data used for analysis (.xlsx and .csv)
figures/        Plots and screenshots
```

Raw exports are preserved unmodified so that every processed value can be traced back to its
source.

---

## Tools

- XFLR5 v6.62 / XFOIL — panel method baseline
- OpenFOAM — 2D RANS solver (Phase 1 onward)
- Python — geometry generation and post-processing
- Microsoft Excel — initial data reduction

---

## References

To be completed with full citations as each source is used.

- Drela, M. (1989). *XFOIL: An Analysis and Design System for Low Reynolds Number Airfoils.*
- NASA Turbulence Modeling Resource — 2D NACA 0012 validation case.
- Abbott, I.H. and von Doenhoff, A.E. *Theory of Wing Sections.*
- Zerihan, J. and Zhang, X. (2000). *Aerodynamics of a Single Element Wing in Ground Effect.*
  Journal of Aircraft. (Phase 2)
