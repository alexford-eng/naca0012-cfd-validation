# Sources

Provenance for all third-party material in this folder. Nothing in `references/` is my own
work. My own output is in `figures/` and `data/`.

**Note on the primary source location:** the NASA Turbulence Modeling Resource has moved from
`turbmodels.larc.nasa.gov` to `tmbwg.github.io/turbmodels`. Older citations in the literature
point to the retired domain. All URLs below are the current ones, accessed 28 August 2026.

---

## Reference figures

### `nasa_tmr_val_clcd_experimental.png`
Experimental lift curve and drag polar for the NACA 0012 at Re = 6 million.
Source: https://tmbwg.github.io/turbmodels/naca0012_val.html

Plotted data attributable to:
- Abbott, I. H. and von Doenhoff, A. E., *Theory of Wing Sections*, Dover Publications,
  New York, 1959. **Untripped.**
- Ladson, C. L., "Effects of Independent Variation of Mach and Reynolds Numbers on the
  Low-Speed Aerodynamic Characteristics of the NACA 0012 Airfoil Section," NASA TM 4074,
  October 1988. **Tripped.**
- Gregory, N. and O'Reilly, C. L., "Low-Speed Aerodynamic Characteristics of NACA 0012
  Aerofoil Sections, including the Effects of Upper-Surface Roughness Simulating Hoar
  Frost," R&M 3726, January 1970. **Tripped, Re = 3 million.**
- McCroskey, W. J., "A Critical Assessment of Wind Tunnel Results for the NACA 0012
  Airfoil," AGARD CP-429, July 1988; also NASA TM 100019, October 1987.
  https://ntrs.nasa.gov/citations/19880002254

### `nasa_tmr_val_sa_clcd_cfd.png`
Spalart-Allmaras CFD results from seven codes, with Ladson tripped experimental data.
Source: https://tmbwg.github.io/turbmodels/naca0012_val_sa.html

### `nasa_tmr_val_sa_cp_cf_*.png`
Pressure coefficient and skin friction coefficient distributions against x/c at
alpha = 0, 10 and 15 degrees.
Source: https://tmbwg.github.io/turbmodels/naca0012_val_sa.html

Experimental symbols on the Cp plots are from Gregory and O'Reilly (cited above). The Cf
plots show CFD results only, as surface shear stress is not measured in these experiments.

---

## Reference data files

Retrieved from https://tmbwg.github.io/turbmodels/naca0012_val_sa.html and kept under their
original filenames so they can be traced back to source.

| File | Contents |
|------|----------|
| `n0012clcd_cfl3d_sa.dat` | CFL3D lift and drag coefficients |
| `n0012cp_cfl3d_sa.dat` | CFL3D surface pressure coefficient distribution |
| `n0012cf_cfl3d_sa.dat` | CFL3D surface skin friction coefficient distribution |

These are **CFD results, not experimental measurements.** The TMR page states that only the
CFL3D data files are provided; the experimental points appear as plotted symbols only. To
obtain experimental values numerically, the original reports would need to be consulted
via NTRS.

Case conditions: M = 0.15, Re = 6 million based on chord, boundary layers fully turbulent.
Grid 897x257 for all codes except GGNS, which is grid-adaptive.

---

## Software

- XFLR5 v6.62, A. Deperrois. https://sourceforge.net/projects/xflr5/
- XFOIL, M. Drela, Massachusetts Institute of Technology.
  *Citation to be completed once the original paper has been read.*

---

## Reported code-to-code agreement

The TMR page reports that the seven independent codes agree to within 1% in lift and 4% in
drag on this case. This sets a practical floor on the numerical uncertainty that can be
claimed for any comparison against these results.
