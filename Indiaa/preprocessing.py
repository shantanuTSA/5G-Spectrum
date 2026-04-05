import pandas as pd

# Load your Excel file (the one with Percent Error column)
df = pd.read_excel("india_auction_data.xlsx")   # or test_predictions.xlsx

# Keep only rows where Percent Error is between -20% and +20%
df_filtered = df[
    (df["Percent Error"] <= 10) &
    (df["Percent Error"] >= -10)
]

# Save cleaned file
df_filtered.to_excel("Cleaned_indian_auction_data.xlsx", index=False)

print("✅ Filtered file saved as filtered_predictions.xlsx")