import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# ----------------------------
# Load dataset
# ----------------------------
df = pd.read_excel("india_auction_data.xlsx")

# ----------------------------
# Keep selected columns
# ----------------------------
columns = [
'Year',
'NoBidders',
'availableSpectrumPaired',
'availableSpectrumUnpaired',
'freqBand',
'FreqMHz',
'region',
'blockFreq',
'LicenceDuration',
'PopCovered',
'reservePriceLocal',
'SpectrumAvailable',
'SpectrumAllotted',
'PPP',
'GDPCap',
'headlinePriceLocal'
]

df = df[columns]

# ----------------------------
# Handle missing values
# ----------------------------
df = df.dropna()

# ----------------------------
# Encode categorical columns
# ----------------------------
df = pd.get_dummies(df, columns=['freqBand', 'region', 'blockFreq'])

# ----------------------------
# Split features and target
# ----------------------------
X = df.drop("headlinePriceLocal", axis=1)
y = df["headlinePriceLocal"]

# ----------------------------
# Train-test split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------
# Train model
# ----------------------------
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------------
# Predictions
# ----------------------------
predictions = model.predict(X_test)

# ----------------------------
# Accuracy metrics
# ----------------------------
r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print("R² Score:", r2)
print("Mean Absolute Error:", mae)

# ----------------------------
# Create comparison dataframe
# ----------------------------
comparison = pd.DataFrame({
    "Actual Headline Price": y_test.values,
    "Predicted Headline Price": predictions
})

# Optional: add prediction error
comparison["Error"] = comparison["Actual Headline Price"] - comparison["Predicted Headline Price"]

# ----------------------------
# Save results to Excel
# ----------------------------
comparison.to_excel("headline_price_predictions.xlsx", index=False)

print("Comparison file saved as headline_price_predictions.xlsx")



