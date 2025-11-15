# ⚡ EV Price Prediction – Week 1 – Problem Definition, Dataset Loading, EDA, and Data Cleaning

📘 Overview  
During Week 1, the focus was on understanding the EV price prediction problem, preparing the dataset, performing exploratory analysis, and cleaning the data for machine-learning tasks in Week 2.  
The week included loading the raw dataset, examining its structure, creating meaningful visualizations, and generating a cleaned dataset ready for modeling.

🎯 Objectives  
- Define the regression problem and identify the target variable  
- Load and examine the raw dataset  
- Perform Exploratory Data Analysis (EDA)  
- Visualize important trends and correlations  
- Clean the dataset by handling missing and inconsistent values  
- Export a clean dataset for Week-2 model training  

🧠 Problem Statement  
The goal for Week 1 was to understand how economic, policy, and environmental factors influence the **average electric vehicle cost**.  
This required analyzing the dataset to uncover trends, distribution patterns, and variable relationships before building models in later weeks.

📊 Dataset Used  
**Dataset:** `ev_adoption_dataset_Raw.csv`

**Source:** [EV Adoption Trends Worldwide (2015–2023)](https://www.kaggle.com/datasets/khushikyad001/ev-adoption-trends-worldwide-20152023) 

**Key Columns**
| Column | Description |
|--------|-------------|
| year | Year of observation |
| country | Country/region |
| avg_cost_ev | Target variable — average EV cost |
| ev_percentage_share | Share of EVs in total vehicles |
| charging_stations_count | Number of charging stations |
| avg_cost_gasoline_vehicle | Average cost of gasoline vehicles |
| gov_incentive_amount | Government incentive amount |
| co2_emissions_per_vehicle | CO₂ emissions per vehicle |
| fuel_price_per_liter | Fuel price in the region |
| electricity_price_per_kWh | Electricity cost per unit |

🔧 Tools & Libraries  
| Category | Libraries / Tools |
|----------|--------------------|
| Data Handling | Pandas |
| Visualization | Matplotlib, Seaborn |
| Uploading (Colab) | google.colab.files |
| Environment | Google Colab / Python 3.10+ |

🚀 Workflow Summary  

### Step 1 – Load Raw Dataset
Uploaded the file `ev_adoption_dataset_Raw.csv` in Google Colab and loaded it using Pandas.

### Step 2 – Perform EDA
- Viewed the first few rows of the dataset  
- Checked data types and null values  
- Calculated summary statistics  
- Analyzed correlations with the target variable `avg_cost_ev`

### Step 3 – Create Visualizations
- Average EV Cost Over Time  
- Government Incentive Amount vs EV Cost  
- Correlation Heatmap to understand feature relationships  

### Step 4 – Clean Dataset
- Removed rows with missing values  
- Exported cleaned dataset as `ev_adoption_dataset_clean.csv`  
- Prepared dataset for Week-2 model training  

📈 Insights & Observations

- EV cost shows a clear trend across different years.  
- Government incentive appears to influence EV pricing.  
- Several features, such as fuel price, emissions, and incentives, show noticeable correlation with EV cost.  
- Some countries have significantly higher pricing patterns, indicating regional variations.  
- Cleaning the dataset improved consistency and removed noisy records, making it ready for modeling.  

💾 Saved Outputs

| File Name | Description |
|-----------|-------------|
| `ev_adoption_dataset_Raw.csv` | Original dataset uploaded for analysis |
| `ev_adoption_dataset_clean.csv` | Cleaned dataset ready for Week-2 modeling |
| `Week1.ipynb` | Notebook containing all Week-1 code, EDA, and visualizations |

## 📊 Data Visualizations

### 📈 Average EV Cost Over Time
<p align="center">
  <img src="https://github.com/Rmjr007/Week-1/blob/e3ec8337b3b5918d15f105663cd1ef81adeb6643/Average%20EV%20Cost%20Over%20Time.png" width="600">
</p>

### 💰 Government Incentive vs Average EV Cost
<p align="center">
  <img src="https://github.com/Rmjr007/Week-1/blob/2d8498154e078b40f3cf9a4ac3eabf003237ce85/Government%20Incestive%20vs.%20Average%20EV%20Cost.png" width="600">
</p>

### 🔥 Correlation Heatmap of All Numerical Features
<p align="center">
  <img src="images/correlation_heatmap.png" width="600">
</p>


👩‍💻 Contributor

- **Rahul Majumder** — Project Developer  

> *“Week-1 successfully built the analytical foundation by transforming raw EV data into clean, structured insights for predictive modeling.”*
