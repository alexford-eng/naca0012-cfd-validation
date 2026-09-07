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

Thin aerofoil theory assumes zero thickness and zero viscocity, so a +1.0% difference between it and my 
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

