## Section 1: Phase 0, XFOIL baseline

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
| Difference from thin-aerofoil theory | +1.0% |
| Cl at alpha = 5 deg | 0.5603 |
| Cd at alpha = 0 deg | 0.00507 |
| Upper surface transition at alpha = 0 | x/c = 0.4119 |
| Lower surface transition at alpha = 0 | x/c = 0.4119 |

Thin aerofoil theory assumes zero thickness and zero viscosity, so a +1.0% difference between it and my 
result is to be expected.                                                                             
                                                                               
The realistic, finite thickness raises the gradient while the boundary-layer displacement reduces it. 
At Re = 6.0 x 10^6, the boundary layer is thin so the thickness has a slightly more significant effect.
This is supported by the fact that the gradient from 0-1 degrees is 0.113/deg, but as the boundary layer 
thickens, it decreases to 0.105/deg between 7.5-8 degrees.

### Internal consistency checks

Cl = 0.0000 and Cm = 0.0000 at alpha = 0 degrees, which is expected since the aerofoil is symmetrical
so should produce zero lift with a zero degree angle of incidence.                              
The upper and lower transition are identical (x/c = 0.4119 at alpha = 0 degrees), so the flow field is
symmetrical as would be expected.                                                             
                                          
The transition moves forwards on the upper surface (0.412 to 0.008) and towards the tail on the lower 
surface (0.412 to 1.00) as alpha increases, correctly demonstrating the strengthening unfavourable
pressure gradient on the top side and the increasingly favourable gradient on the bottom side.             

The centre of pressure remained stable at x/c 0.238-0.247.

### Comparison against NASA

Comparing against the NASA seven-code mean, with Prandtl-Glauert correction applied to lift:              
Cl: +3.8% (alpha = 10 degrees), +3.9% (alpha = 15 degrees)                                        
Cd: -37.9% (alpha = 0 degrees), -20.9% (alpha = 10 degrees), -23.8% (alpha = 15 degrees)                    
     
XFOIL runs free transition (the flow is laminar until 41% from the leading edge at alpha = 0), whereas NASA
runs fully turbulent from the leading edge. Since turbulent boundary layers have 2-3x the skin friction,
my drag came out as much lower. Turbulent layers are also thicker, causing decambering, meaning the lift
in my results is higher.

This explanation is supported by the fact the drag discrepancy between mine and NASA's results decreased as
alpha rose and the laminar section of the aerofoil got smaller (went from 37.9% to 20.9% & 23.8%).

## Section 2: Phase 1 setup

I used NASA's grids instead of self-generated ones to remove mesh quality as a possible variable that may affect results, so a better comparison on identical cells could be attained, and because NASA's grids are purpose built for grid convergence. Although mesh generation is not a skill demonstrated in this phase, since there is no published grid to be used in phase 2, it will be used then.

OpenFOAM was used as the solver, with a steady-state incompressible flow. I used Re = 6 x 10^6 with ν = 1.6667 x 10^-7, U = 1 and c = 1.

Spalart-Allmaras was used as the turbulence model, with nuTilda_∞ = 3ν to match NASA's stated value. The simulation was also wall-resolved with no wall functions ( `nutLowReWallFunction`).

Model verification was performed, with all Spalart-Allmaras constants being checked against TMR specification and confirmed identical (sigmaNut 0.66666, kappa 0.41, Cb1 0.1355, Cb2 0.622, Cw2 0.3, Cw3 2, Cv1 7.1).

NASA used standard Spalart-Allmaras with ft2 active, while OpenFOAM defaults to SA-noft2 (`ft2 false`). TMR states these should give very similar results when the freestream turbulence variable is large enough to override ft2, which it is at 3ν.

## Section 3: Mesh Independence

### at alpha = 0 degrees

|Grid	|Cells|	Cd	|vs NASA	|y+ avg	|Max non-orth|
|---|---|---|---|---|---|
|113×33	|3,584	|0.016176	|+98.0%	|1.648	|85.7°|
|225×65	|14,336	|0.009644	|+18.0%	|0.517	|77.4°|
|440×129	|57,344	|0.008459	|+3.5%	|0.213	|52.4°|
|897×257	|229,376	|0.008487*	|+3.9%	|0.099	|19.8°|

The order of convergence was found to be 2.46, observed from grids 1-3. Error reduced 5.43x, then 5.09x (similar factors across 2 independent refinements).
Mesh quality consistently improved, with the maximum non-orthogonality decreasing from 85.7 degrees for the coarsest grid to 19.8 degrees for the most refined one. The amount of severely non-orthogonal faces also decreased from 166 to 0 as the grid became more refined.
the y+ value was below 1 from the second grid onward, reaching a 0.099 average on the finest, and being wall-resolved throughout. 
Grids 3 and 4 agree to 0.33%, and the solution is mesh independent.

## Section 4: The limit cycle

*897x257 developed a numerical limit cycle with a period of ~3500 iterations between 8500-12000. Cl was oscillating by +-0.0035 around a mean of -1.6 x 10^-5. The stated value is a period-averaged mean, not a converged value. Cd oscillated over only +-0.20%. This only happened on the finest grid because more coarse meshes carry numerical dissipation which damps weakly unstable modes (refining removes artificial damping). The progression can be seen across all 4 grids: the coarsest grid oscillated between 2 values, the 440x120 grid drifted monotonically, and the finest grid limit-cycled. The amount of iterations required for the values to settle also scales with refinement, with the coarsest grid requiring only a few hundred iterations to converge, whereas the finest grid did not reach a fixed point even after 12000 iterations.

I attempted to use Richardson extrapolation, which predicted a grid-independent Cd of 0.008197 (+0.33% compared to NASA) on grids 1-3, but grid 4 (the finest grid) did not confirm this, and the change between grid 3 and 4 reversed the sign, meaning convergence is not monotonic across all four points and the extrapolation is invalid, so this was retracted.

## Section 5: Surface comparisons 

Used the `wallShearStress` function object and `surfaces` sampling on the aerofoil patch, got 256 face-centre values at the spanwise midplane and did no interpolation. 
Non-dimensionalisation: Cp = 2p
                        Cf = -2tau_x (magUInf=1)
The OpenFOAM wall shear stress sign convention is opposite to CFL3D's, which was discovered by observing that the obtained curves were exact mirror images through zero.
The Cp results showed upper and lower surfaces coinciding, due to the aerofoil's symmetry, and both track CFL3D almost exactly from stagnation (Cp ≈ 1.0) to the suction peak (Cp ≈ -0.4 at x/c ≈ 0.1), until the trailing edge with no systematic error.
The Cf results showed the shape, peak location (at x/c ≈ 0.03) and decay all matching. The only two differences were a ~2% gap in the peak's magnitude, and a small divergence at x/c > 0.98 (where CFL3D's own file header documents high error).

<img width="1062" height="703" alt="cf_comparison_alpha0_FIXED" src="https://github.com/user-attachments/assets/96683e1a-8418-408a-a56b-8b7df004899d" />

<img width="1062" height="703" alt="cf_comparison_alpha0_FIXED" src="https://github.com/user-attachments/assets/90858ab1-d700-43a3-bbce-e4b7efd269e2" />

## Section 6: The residual difference

Magnitude: +3.6% against CFL3D, +3.9% against the seven-code mean.
The seven reference codes differ from each other by 2.2% in the same conditions, with TURNS being 1.64% above the mean. So, although my difference is outside this difference, it is not significantly out of their range.

When trying to understand the cause of this difference, a discretisation error was ruled out since the two most fine grids differed by only 0.3%. Spalart-Allmaras constants were also confirmed to be identical, and there is no observable structural error in the flow field since the Cp and Cf values matched almost exactly (apart from a localised discrepancy in Cf in a resolution-sensitive region).

The impact of modelling incompressible flow instead of M = 0.15 has not been tested so cannot be ruled out, and neither has convection scheme differences against CFL3D. No scheme or setting was varied to try to force my results to match CFL3D's, and changes were only made where there was a documented difference from the reference, independent of whether it improved the similarity between the sets of results.

## Section 7: Limitations

The simulation is fully turbulent with no transition model, which is unrealistic for a clean aerofoil at Re = 6.0 x 10^6 (natural transition occurs around x/c ≈ 0.41 in XFOIL). This choice was made to match NASA's cases and the tripped data they validate against. The effect of this was quantified in phase 0, where it was found that free transition reduces drag by 21-38%.

Modelled using incompressible flow, instead of M = 0.15 which was the reference.

The finest grid didn't fully converge, and period-averaged values were reported.

NASA's grids contain a documented ~10^-8 non-closure at the tailing edge due to a typo in the aerofoil equation.

