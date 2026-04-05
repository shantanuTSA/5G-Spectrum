import pandas as pd

# Load file
df = pd.read_csv("/home/shantanu/Desktop/SEM 4/Projects/Sridhar_Sir_work/ML/DatabaseCountriesForDiff.csv")

# Define column names
headline_col = "headlinePriceLocal"
reserve_col = "reservePriceLocal"

# --- Clean and convert to numeric ---

# Remove commas (if any) and convert to numeric
df[headline_col] = (
    df[headline_col]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df[reserve_col] = (
    df[reserve_col]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df[headline_col] = pd.to_numeric(df[headline_col], errors="coerce")
df[reserve_col] = pd.to_numeric(df[reserve_col], errors="coerce")

# --- Create new columns ---

# 1️⃣ Absolute difference
df["Price Difference"] = df[headline_col] - df[reserve_col]

# 2️⃣ Percentage increase
df["Percentage Increase (%)"] = (
    (df[headline_col] - df[reserve_col]) / df[reserve_col]
) * 100

# Optional: round percentage
df["Percentage Increase (%)"] = df["Percentage Increase (%)"].round(2)

# Save new file
df.to_csv("Auction_with_price_difference.csv", index=False)

print("New CSV created successfully.")
