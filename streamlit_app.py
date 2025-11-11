import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="EV Policy Simulator 📈",
    page_icon="🚗",
    layout="wide"
)

st.title("📈 EV Policy Simulator Dashboard")
st.markdown("Use this app to predict an outcome based on electric vehicle policy and economic factors.")

# -------------------------------------------------------
# Load trained model and scaler
# -------------------------------------------------------

# Define file paths
MODEL_PATH = "models/ev_policy_best_model.pkl"
SCALER_PATH = "models/scaler.pkl"

# Helper function to load files
@st.cache_resource
def load_model(model_path, scaler_path):
    # Check for model file
    if not os.path.exists(model_path):
        st.error(f"**Error:** Model file not found at `{model_path}`.")
        return None, None
        
    # Check for scaler file
    if not os.path.exists(scaler_path):
        st.error(f"**Error:** Scaler file not found at `{scaler_path}`.")
        return None, None
        
    # Load files
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except Exception as e:
        st.error(f"Error loading model or scaler: {e}")
        return None, None

model, scaler = load_model(MODEL_PATH, SCALER_PATH)

# Define the exact feature names the model expects
EXPECTED_FEATURES = [
    'total_vehicles_registered',
    'ev_percentage_share',
    'charging_stations_count',
    'avg_cost_ev',
    'avg_cost_gasoline_vehicle',
    'gov_incentive_amount',
    'co2_emissions_per_vehicle',
    'fuel_price_per_liter',
    'electricity_price_per_kwh'
]

# -------------------------------------------------------
# User Input Section
# -------------------------------------------------------
st.subheader("🔧 Enter Policy & Economic Data")

if model and scaler:
    col1, col2, col3 = st.columns(3)

    with col1:
        total_vehicles = st.number_input("Total Vehicles Registered", value=1000000.0, format="%.2f")
        ev_share = st.number_input("EV Percentage Share (%)", value=5.0, format="%.2f")
        charging_stations = st.number_input("Charging Stations Count", value=5000.0, format="%.2f")

    with col2:
        avg_cost_ev = st.number_input("Avg. Cost of EV ($)", value=35000.0, format="%.2f")
        avg_cost_gas = st.number_input("Avg. Cost of Gasoline Vehicle ($)", value=25000.0, format="%.2f")
        incentive = st.number_input("Government Incentive ($)", value=7500.0, format="%.2f")

    with col3:
        co2_emissions = st.number_input("CO2 Emissions per Vehicle (g/km)", value=120.0, format="%.2f")
        fuel_price = st.number_input("Fuel Price (per Liter) ($)", value=1.5, format="%.2f")
        electricity_price = st.number_input("Electricity Price (per kWh) ($)", value=0.15, format="%.2f")

    # -------------------------------------------------------
    # Predict
    # -------------------------------------------------------
    if st.button("🔮 Run Simulation"):
        # Create DataFrame with the exact feature names
        input_data = pd.DataFrame(
            data=[[
                total_vehicles,
                ev_share,
                charging_stations,
                avg_cost_ev,
                avg_cost_gas,
                incentive,
                co2_emissions,
                fuel_price,
                electricity_price
            ]],
            columns=EXPECTED_FEATURES
        )
        
        st.info("Calculating... (Scaling data and running prediction)")
        
        try:
            # Scale Data
            scaled_data = scaler.transform(input_data)
            
            # Predict
            prediction = model.predict(scaled_data)[0]
            
            st.success(f"**Predicted Outcome:** {prediction:,.2f}")
            st.caption("(Note: This is the raw output from the linear regression model.)")
            st.balloons()
            
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

else:
    st.error("Application cannot start. Please check file paths and ensure `models/ev_policy_best_model.pkl` and `models/scaler.pkl` are in your GitHub repository.")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.markdown("---")
st.caption("A Streamlit app built to work with `ev_policy_best_model.pkl`.")
