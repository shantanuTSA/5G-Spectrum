import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your file
df = pd.read_excel("full_predictions.xlsx")

# ----------------------------
# Create correct columns
# ----------------------------

df["HL_MHz_Pop"] = df["Predicted Headline Price"] / (
    df["SpectrumAllotted"] * df["PopCovered"]
)

df["RP_MHz_Pop"] = df["reservePriceLocal"] / (
    df["SpectrumAllotted"] * df["PopCovered"]
)

# ----------------------------
# Clean invalid values
# ----------------------------
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(subset=["HL_MHz_Pop", "RP_MHz_Pop"])

# ----------------------------
# Plot
# ----------------------------
x_vals = df["RP_MHz_Pop"]
plt.plot(x_vals, x_vals, linestyle='--')
plt.figure()


plt.scatter(df["RP_MHz_Pop"], df["HL_MHz_Pop"], alpha=0.6)

plt.xlabel("Reserve Price per MHz per Population (RP/MHz/Pop)")
plt.ylabel("Headline Price per MHz per Population (HL/MHz/Pop)")
plt.title("HL vs RP per MHz per Population")

plt.grid()

plt.savefig("hl_vs_rp_corrected.png")
plt.close()

print("✅ Graph saved as hl_vs_rp_corrected.png")