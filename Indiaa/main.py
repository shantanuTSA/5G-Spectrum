import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Cleaned_indian_auction_data.xlsx")

# Select final columns
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

# Handle missing values
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna("Unknown")

# Encode categorical columns
df = pd.get_dummies(df, columns=['freqBand', 'region', 'blockFreq'])

# Split features and target
X = df.drop("headlinePriceLocal", axis=1)

#  LOG TRANSFORM
y = np.log(df["headlinePriceLocal"])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.24, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=650,
    random_state=42
)

model.fit(X_train, y_train)

# TEST SET PREDICTIONS (for accuracy)
pred_test_log = model.predict(X_test)

pred_test = np.exp(pred_test_log)
y_test_actual = np.exp(y_test)

# Accuracy metrics
r2 = r2_score(y_test_actual, pred_test)
mae = mean_absolute_error(y_test_actual, pred_test)

print("R² Score:", r2)
print("Mean Absolute Error:", mae)

# Save TEST SET comparison
# test_comparison = pd.DataFrame({
#     "Actual Headline Price": y_test_actual,
#     "Predicted Headline Price": pred_test
# })

# test_comparison["Error"] = (
#     test_comparison["Actual Headline Price"] -
#     test_comparison["Predicted Headline Price"]
# )

# test_comparison["Percent Error"] = (
#     test_comparison["Error"] /
#     test_comparison["Actual Headline Price"]
# ) * 100

# test_comparison.to_excel("test_predictions.xlsx", index=False)

# print(" Test set file saved: test_predictions.xlsx")

# FULL DATASET PREDICTIONS (all rows)
full_pred_log = model.predict(X)

full_pred = np.exp(full_pred_log)
y_actual_full = np.exp(y)

full_comparison = pd.DataFrame({
    "Actual Headline Price": y_actual_full,
    "Predicted Headline Price": full_pred
})

full_comparison["Error"] = (
    full_comparison["Actual Headline Price"] -
    full_comparison["Predicted Headline Price"]
)

full_comparison["Percent Error"] = (
    full_comparison["Error"] /
    full_comparison["Actual Headline Price"]
) * 100

full_comparison.to_excel("full_predictions.xlsx", index=False)

print(" Full dataset file saved: full_predictions.xlsx")


#function to predict headline price for new input

def predict_headline_price(
    Year,
    NoBidders,
    availableSpectrumPaired,
    availableSpectrumUnpaired,
    freqBand,
    FreqMHz,
    region,
    blockFreq,
    LicenceDuration,
    PopCovered,
    reservePriceLocal,
    SpectrumAvailable,
    SpectrumAllotted,
    PPP,
    GDPCap
):
    import pandas as pd
    import numpy as np

    # Create input dataframe
    input_dict = {
        'Year': [Year],
        'NoBidders': [NoBidders],
        'availableSpectrumPaired': [availableSpectrumPaired],
        'availableSpectrumUnpaired': [availableSpectrumUnpaired],
        'freqBand': [freqBand],
        'FreqMHz': [FreqMHz],
        'region': [region],
        'blockFreq': [blockFreq],
        'LicenceDuration': [LicenceDuration],
        'PopCovered': [PopCovered],
        'reservePriceLocal': [reservePriceLocal],
        'SpectrumAvailable': [SpectrumAvailable],
        'SpectrumAllotted': [SpectrumAllotted],
        'PPP': [PPP],
        'GDPCap': [GDPCap]
    }

    input_df = pd.DataFrame(input_dict)

    # Encode categorical variables SAME WAY as training
    input_df = pd.get_dummies(input_df)

    # Align columns with training data
    input_df = input_df.reindex(columns=X.columns, fill_value=0)

    # Predict (log scale)
    pred_log = model.predict(input_df)

    # Convert back
    prediction = np.exp(pred_log)

    return prediction[0]

price = predict_headline_price(
    Year=2010,
    NoBidders=9,
    availableSpectrumPaired=710,
    availableSpectrumUnpaired=0,
    freqBand="2.1 GHz",
    FreqMHz=2100,
    region="Delhi",
    blockFreq="1959-1964 MHz",
    LicenceDuration=20,
    PopCovered=17403916,
    reservePriceLocal=3200000000,
    SpectrumAvailable=710,
    SpectrumAllotted=10,
    PPP=14.2,
    GDPCap=4405
)

print("Predicted Headline Price:", price)

print(" Accuracy: ", r2* 100, "%")



percent_changes = list(range(0, 101, 5))
total_revenues = []

for pct in percent_changes:
    
    df_temp = pd.read_excel("Cleaned_indian_auction_data.xlsx")

    df_temp = df_temp[columns]

    for col in df_temp.select_dtypes(include=['float64', 'int64']).columns:
        df_temp[col] = df_temp[col].fillna(df_temp[col].median())

    for col in df_temp.select_dtypes(include=['object']).columns:
        df_temp[col] = df_temp[col].fillna("Unknown")

    df_temp["reservePriceLocal"] = df_temp["reservePriceLocal"] * (1 - pct/100)

    df_temp = pd.get_dummies(df_temp, columns=['freqBand', 'region', 'blockFreq'])

    X_temp = df_temp.reindex(columns=X.columns, fill_value=0)

    pred_log = model.predict(X_temp)
    pred = np.exp(pred_log)

    total_revenue = pred.sum()

    total_revenues.append(total_revenue)

# Plot graph
plt.figure()
plt.plot(percent_changes, total_revenues, marker='o')
plt.xlabel("Percentage Decrease in Reserve Price (%)")
plt.ylabel("Total Predicted Revenue")
plt.title("Revenue vs Reserve Price Reduction")
plt.grid()
plt.savefig("revenue_vs_reserve_price.png")
print("Graph saved as revenue_vs_reserve_price.png")


