# Module 1: Data Preprocessing & EDA (Air Quality)

This module focuses on preparing and analyzing air quality datasets to understand pollutant trends and build a foundation for forecasting.

## 📊 Datasets
- **CPCB**: Central Pollution Control Board (India)  
- **OpenAQ**: Open-source global air quality dataset  

> Datasets can be stored in `data/` or downloaded via APIs.

## 🔧 Steps Performed
1. **Download & Load Data**
   - Fetched datasets from CPCB and OpenAQ
   - Handled missing values and outliers

2. **Data Preprocessing**
   - Standardized column names
   - Converted timestamps to datetime objects
   - Removed duplicates
   - Imputed missing pollutant readings

3. **Exploratory Data Analysis (EDA)**
   - Checked distribution of pollutants (PM2.5, PM10, NO2, SO2, CO, O3, etc.)
   - Trend analysis over time (daily, weekly, monthly)
   - Correlation heatmaps between pollutants

4. **Resampling & Feature Engineering**
   - Resampled to hourly/daily averages
   - Created lag features for forecasting
   - Added rolling averages (e.g., 7-day moving average)

# --------------------------------------------------------
# DATA PREPROCESSING IN PYTHON
# --------------------------------------------------------
# Data preprocessing is an essential step before applying
# ML algorithms. It ensures the data is clean and suitable
# for analysis.
#
# Common steps include:
# 1. Handling Missing Values
# 2. Feature Scaling
# 3. Encoding Categorical Data
# --------------------------------------------------------

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# -------------------------
# 1. HANDLING MISSING VALUES
# -------------------------

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [25, None, 30, 22],
    "Salary": [50000, 60000, None, 55000],
    "City": ["Delhi", "Mumbai", "Chennai", "Delhi"]
}

df = pd.DataFrame(data)
print("🔹 Original Data:\n", df)

# Filling missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)         # fill with mean
df["Salary"].fillna(df["Salary"].median(), inplace=True) # fill with median

print("\n✅ After Handling Missing Values:\n", df)


# -------------------------
# 2. FEATURE SCALING
# -------------------------
# Scaling brings all numeric values into the same range (e.g., 0–1),
# so that no feature dominates others.

scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df[["Age", "Salary"]])  # only numeric columns
scaled_df = pd.DataFrame(scaled_values, columns=["Age_Scaled", "Salary_Scaled"])

print("\n✅ After Feature Scaling:\n", scaled_df)


# -------------------------
# 3. ENCODING CATEGORICAL DATA
# -------------------------
# Machine learning models require numerical input.
# So categorical columns must be encoded.

# Label Encoding (assigns numbers to categories)
encoder = LabelEncoder()
df["City_Label"] = encoder.fit_transform(df["City"])
print("\n✅ After Label Encoding:\n", df[["City", "City_Label"]])

# One-Hot Encoding (creates separate columns for each category)
ohe_df = pd.get_dummies(df["City"], prefix="City")
print("\n✅ After One-Hot Encoding:\n", ohe_df)
