import streamlit as st
import numpy as np
import pickle

# Page setup
st.set_page_config(
    page_title="Fitness Outcome Predictor",
    page_icon="💪",
    layout="centered"
)

st.title("💪 Fitness Outcome Prediction")
st.write("Enter your details to predict your fitness outcome score")

# Load trained model (from your notebook)
model = pickle.load(open("fitness_model.pkl", "rb"))

# ---------------- INPUTS ----------------
st.header("👤 Body Details")
weight_kg = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
bmi = st.number_input("BMI", 10.0, 50.0, 23.0)

st.header("🥗 Nutrition Details")
calories = st.number_input("Daily Calories Intake", 0, 6000, 2200)
protein_ratio = st.slider("Protein Ratio (%)", 0, 100, 25)
water_liters = st.number_input("Water Intake (liters)", 0.0, 10.0, 3.0)

st.header("🏋️ Workout Details")
workout_minutes = st.slider("Workout Duration (minutes)", 0, 300, 45)
workout_days = st.slider("Workout Days per Week", 0, 7, 4)
workout_intensity = st.selectbox(
    "Workout Intensity",
    ["Low", "Medium", "High"]
)

# Encode workout intensity (MUST match notebook encoding)
intensity_mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}
workout_intensity_encoded = intensity_mapping[workout_intensity]

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Fitness Outcome"):

    user_input = np.array([[
        weight_kg,
        bmi,
        calories,
        protein_ratio,
        water_liters,
        workout_minutes,
        workout_days,
        workout_intensity_encoded
    ]])

    prediction = model.predict(user_input)[0]

    st.success("Prediction Successful ✅")
    st.metric("Fitness Outcome Score", round(prediction, 2))

    # Interpretation
    if prediction < 50:
        st.error("Poor fitness outcome ⚠️")
    elif prediction < 70:
        st.warning("Average fitness outcome 🙂")
    elif prediction < 85:
        st.info("Good fitness outcome 💪")
    else:
        st.success("Excellent fitness outcome 🔥")
