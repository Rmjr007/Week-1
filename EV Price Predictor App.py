import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------------

# Load trained model and scaler

# -------------------------------------------------------

# Note: For this to work on Render, you MUST have a folder named 'models'
# in your GitHub repository, and it must contain:
# - ev_price_model.pkl
# - scaler.pkl

model = joblib.load("models/ev_price_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# -------------------------------------------------------

# Streamlit Page Configuration

# -------------------------------------------------------

st.set_page_config(
page_title="EV Price Predictor ⚡",
page_icon="🚗",
layout="centered"
)

st.title("⚡ Electric Vehicle Price Prediction Dashboard")
st.markdown("Use this app to predict the **price range** of an electric vehicle based on its specifications.")

# -------------------------------------------------------

# User Input Section

# -------------------------------------------------------

st.subheader("🔧 Enter EV Specifications")

col1, col2 = st.columns(2)

with col1:
    battery = st.number_input("🔋 Battery Capacity (kWh)", min_value=10.0, max_value=200.0, value=60.0)
    accel = st.number_input("🚀 0 - 100 km/h (sec)", min_value=2.0, max_value=20.0, value=7.0)
    speed = st.number_input("🏎️ Top Speed (km/h)", min_value=50.0, max_value=400.0, value=180.0)

with col2:
    range_km = st.number_input("🔋 Range (km)", min_value=50.0, max_value=800.0, value=400.0)
    efficiency = st.number_input("⚙️ Efficiency (Wh/km)", min_value=100.0, max_value=400.0, value=180.0)
    seats = st.slider("🪑 Number of Seats", 2, 8, 5)


# -------------------------------------------------------

# Prepare DataFrame for Prediction

# -------------------------------------------------------

input_data = pd.DataFrame({
"battery": [battery],
"0 - 100": [accel],
"Top Speed": [speed],
"Range*": [range_km],
"Efficiency*": [efficiency],
"Number_of_seats": [seats]
})

# -------------------------------------------------------

# Scale Data

# -------------------------------------------------------

scaled_data = scaler.transform(input_data)

# -------------------------------------------------------

# Predict Price

# -------------------------------------------------------

if st.button("🔮 Predict Price Range"):
    prediction = model.predict(scaled_data)[0]
    st.success(f"💰 Estimated Price Range: **${prediction:,.2f} USD**")
    st.balloons()


# -------------------------------------------------------

# Footer

# -------------------------------------------------------

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Green Policy Simulator Project")
