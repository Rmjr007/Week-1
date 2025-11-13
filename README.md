# ⚡ EV Price Prediction – Week 1

## 📘 1. Project Overview
This project aims to build a **Machine Learning model** that predicts the **average cost of Electric Vehicles (EVs)** using real-world economic, policy, environmental, and infrastructure-related factors.

**Week 1 focuses on:**
- Defining the prediction problem  
- Loading the dataset in Google Colab  
- Performing Exploratory Data Analysis (EDA)  
- Cleaning and preparing the dataset for Week 2 modeling  

---

## 📊 2. Week 1 Summary
Below is a summary of all tasks completed in Week 1:

### ✔️ Completed Tasks
- Clearly defined the regression problem  
- Identified target and feature variables  
- Uploaded and loaded the raw dataset: `ev_adoption_dataset_Raw.csv`  
- Performed EDA:  
  - First 5 rows  
  - Data types  
  - Null value detection  
  - Descriptive statistics  
  - Correlation insights  
- Created visualizations to explore relationships  
- Cleaned the dataset by removing incomplete rows  
- Saved the processed dataset as `ev_adoption_dataset_clean.csv`  

---

## 🎯 3. Problem Definition

### **Machine Learning Task:**  
Regression

### **Target Variable (y):**  
`avg_cost_ev` — Average cost of an electric vehicle

### **Feature Variables (X):**
| Feature | Description |
|---------|-------------|
| `ev_percentage_share` | EV market share percentage |
| `charging_stations_count` | Count of charging stations |
| `avg_cost_gasoline_vehicle` | Average cost of gasoline vehicles |
| `gov_incentive_amount` | Government incentives for EVs |
| `co2_emissions_per_vehicle` | Emissions per vehicle |
| `fuel_price_per_liter` | Fuel price in that region |
| `electricity_price_per_kWh` | Electricity price |
| `country` | Country (categorical) |
| `year` | Year of data entry |

---

## 💻 4. Required Libraries

### ✔️ All available in Colab:
`pandas
matplotlib
seaborn
google.colab.files`

---

## 🧪 5. How Week-1 Code Was Executed (Google Colab Workflow)

### **Main Notebook:**  
`Week1.ipynb`

### ▶️ Execution Steps
```python```
# 1. Upload the raw dataset
from google.colab import files
uploaded = files.upload()   # Select ev_adoption_dataset_Raw.csv

# 2. Load the dataset
import pandas as pd
df = pd.read_csv("ev_adoption_dataset_Raw.csv")

# 3. Perform EDA (head, info, describe, correlations)

# 4. Clean the dataset
df_clean = df.dropna()

# 5. Save the cleaned file
df_clean.to_csv("ev_adoption_dataset_clean.csv", index=False)` 

---

## 📂 6. Output Files
- ev_adoption_dataset_Raw.csv  
- ev_adoption_dataset_clean.csv  
- Week1.ipynb  

---

## 👨‍💻 Contributor
- **Rahul Majumder** — Project Developer




