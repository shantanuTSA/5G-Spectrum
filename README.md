# 📡 5G Spectrum Auction Analysis & Price Prediction (India + Brazil)

## 🚀 Overview

This project builds a **machine learning-based system** to analyze and predict **5G spectrum auction prices** using real-world auction data from **India and Brazil**.

It goes beyond simple prediction and explores how **auction parameters (like reserve price, spectrum, and competition)** influence final outcomes.

---

## 🎯 Objectives

* Predict **headline auction prices** using ML models
* Analyze the relationship between **reserve price and final revenue**
* Compare auction behavior across **India and Brazil**
* Build a foundation for **auction policy simulation and optimization**

---

## 🧠 Key Concepts

* 📊 **Headline Price** → Final auction selling price
* 💰 **Reserve Price** → Minimum price set by the government
* ⚖️ **Auction Efficiency** → How much price exceeds reserve
* 📈 **Revenue Simulation** → Total predicted auction revenue

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost (for advanced modeling)
* Matplotlib

## ⚙️ How It Works

### 1️⃣ Data Preprocessing

* Select relevant auction features
* Handle missing values
* Encode categorical variables

### 2️⃣ Model Training

* Train ML models (Random Forest / XGBoost)
* Use log transformation for stability

### 3️⃣ Prediction

* Predict headline prices for:

  * Test set
  * Full dataset

### 4️⃣ Evaluation

* R² Score
* Mean Absolute Error
* Percent Error analysis

---



## 🧪 Example Usage

```python
price = predict_headline_price(
    Year=2010,
    NoBidders=9,
    availableSpectrumPaired=710,
    availableSpectrumUnpaired=0,
    freqBand="2.1 GHz",
    FreqMHz=2100,
    region="Delhi",
    LicenceDuration=20,
    PopCovered=17403916,
    reservePriceLocal=3200000000,
    SpectrumAvailable=710,
    SpectrumAllotted=10,
    PPP=14.2,
    GDPCap=4405
)

print("Predicted Headline Price:", price)
```



## 👤 Author

Shantanu

---

## ⭐ If you found this useful, consider starring the repo!
