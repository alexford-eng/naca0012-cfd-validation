# Compares OpenFOAM surface Cp and Cf (449x129 grid, alpha=0) against
# CFL3D reference data from the NASA Turbulence Modeling Resource.
#
# Note: OpenFOAM's wallShearStress sign convention is opposite to CFL3D's.
# Cf = -2*tau_x is used here to match the reference convention.import pandas as pd
import matplotlib.pyplot as plt

# --- read your OpenFOAM surface data ---
p = pd.read_csv(
    "grid_449-129/postProcessing/sampleSurface/5020/p_aerofoilSurface.raw",
    comment="#", sep=r"\s+",
    names=["x", "y", "z", "p"]
)
wss = pd.read_csv(
    "grid_449-129/postProcessing/sampleSurface/5020/wallShearStress_aerofoilSurface.raw",
    comment="#", sep=r"\s+",
    names=["x", "y", "z", "tau_x", "tau_y", "tau_z"]
)

# merge on position (both files list the same 256 face centres)
df = p.merge(wss, on=["x", "y", "z"])

# non-dimensionalise: magUInf = 1, so Cp = 2p, Cf = 2*tau_x
df["Cp"] = 2 * df["p"]
df["Cf"] = -2 * df["tau_x"]

# split by surface using the sign of z
upper = df[df["z"] >= 0].sort_values("x")
lower = df[df["z"] < 0].sort_values("x")
# --- read CFL3D Cp reference (alpha = 0, both surfaces together) ---
with open("references/n0012cp_cfl3d_sa.dat") as f:
    lines = f.readlines()

start = next(i for i, l in enumerate(lines) if 'alpha=0' in l) + 1
end = next((i for i in range(start, len(lines)) if 'zone' in lines[i]), len(lines))

cp_rows = [line.split() for line in lines[start:end] if line.strip()]
cp_cfl3d = pd.DataFrame(cp_rows, columns=["x", "Cp"]).astype(float)

print(f"\nCFL3D Cp alpha=0: {len(cp_cfl3d)} points total (both surfaces)")
print(cp_cfl3d.head())

plt.figure(figsize=(8, 5))
plt.plot(upper["x"], upper["Cp"], "o-", markersize=3, label="OpenFOAM upper (yours)")
plt.plot(lower["x"], lower["Cp"], "s-", markersize=3, label="OpenFOAM lower (yours)")
plt.plot(cp_cfl3d["x"], cp_cfl3d["Cp"], "-", color="black", label="CFL3D (NASA reference)")
plt.gca().invert_yaxis()
plt.xlabel("x/c")
plt.ylabel("Cp")
plt.title("Pressure coefficient, alpha = 0")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("figures/cp_comparison_alpha0.png", dpi=150, bbox_inches="tight")
print("saved figures/cp_comparison_alpha0.png")
print(f"total points: {len(df)}   upper: {len(upper)}   lower: {len(lower)}")
print(upper[["x", "z", "Cp", "Cf"]].head())
# --- read CFL3D reference (alpha = 0, upper surface only) ---
with open("references/n0012cf_cfl3d_sa.dat") as f:
    lines = f.readlines()

# find the alpha=0 zone and read until the next "zone" line or EOF
start = next(i for i, l in enumerate(lines) if 'alpha=0' in l) + 1
end = next((i for i in range(start, len(lines)) if 'zone' in lines[i]), len(lines))

cfl3d_rows = [line.split() for line in lines[start:end] if line.strip()]
cfl3d = pd.DataFrame(cfl3d_rows, columns=["x", "Cf"]).astype(float)

print(f"\nCFL3D alpha=0 upper surface: {len(cfl3d)} points")
print(cfl3d.head())
plt.figure(figsize=(8, 5))
plt.plot(upper["x"], upper["Cf"], "o-", markersize=3, label="OpenFOAM (yours, 449x129)")
plt.plot(cfl3d["x"], cfl3d["Cf"], "-", label="CFL3D (NASA reference)")
plt.xlabel("x/c")
plt.ylabel("Cf")
plt.title("Skin friction coefficient, upper surface, alpha = 0")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("figures/cf_comparison_alpha0.png", dpi=150, bbox_inches="tight")
print("\nsaved figures/cf_comparison_alpha0.png")
