import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("cognitive_score_predictor.pkl")

st.title("🧠 Cognitive Score Predictor")
st.write("Enter the following details to predict your cognitive score:")

# Age
age = st.slider("Age:", 10, 100, 25)

# Gender input
gender = st.selectbox("Select Gender:", ["Female", "Male", "Other"])
gender_map = {"Female": 0, "Male": 1, "Other": 2}
gender_encoded = gender_map[gender]

# Sleep (hours per night)
sleep_hours = st.slider("Average Sleep (hours per night):", 0, 12, 7)

# Stress Level (1-10)
stress_level = st.slider("Stress Level (1 = low, 10 = high):", 1, 10, 5)

# Diet Type
diet = st.selectbox("Select Diet Type:", ["Non-Vegetarian", "Vegetarian", "Vegan"])
diet_map = {label: idx for idx, label in enumerate(["Non-Vegetarian", "Vegetarian", "Vegan"])}
diet_encoded = diet_map[diet]

# Screen Time (hours per day)
screen_time = st.slider("Average Screen Time (hours per day):", 0, 16, 6)

# Exercise Frequency (Low, Medium, High)
exercise = st.selectbox("Exercise Frequency:", ["Low", "Medium", "High"])
exercise_map = {"Low": 0, "Medium": 1, "High": 2}
exercise_encoded = exercise_map[exercise]

# Caffeine Intake
caffeine = st.slider("Caffeine Intake (mg per day):", 0, 1000, 200)

# Reaction Time (ms)
reaction_time = st.slider("Reaction Time (in milliseconds):", 100, 1000, 300)

# Memory Test Score (0-100)
memory_score = st.slider("Memory Test Score (out of 100):", 0, 100, 75)

# Prediction button
if st.button("Predict Cognitive Score"):
    input_data = np.array([[
        age, gender_encoded, sleep_hours, stress_level, diet_encoded,
        screen_time, exercise_encoded, caffeine, reaction_time, memory_score
    ]])
    prediction = model.predict(input_data)[0]
    st.success(f"🧠 Predicted Cognitive Score: {prediction:.2f}")

st.markdown("---")
st.markdown("**Made by Shibaa**")
