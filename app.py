# app.py
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------
# Load model (path-safe)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "insurance_rf_model.pkl"
model = joblib.load(MODEL_PATH)

# -----------------------------
# Page config (phone-friendly)
# -----------------------------
st.set_page_config(page_title="Insurance Cost Estimator", layout="centered")

st.title("Insurance Cost Estimator")
st.caption("Estimate what affects insurance costs • For awareness only • Values shown in KES (estimate)")

st.markdown("---")

# -----------------------------
# Inputs (simple for common users)
# -----------------------------
age = st.number_input("Age", min_value=18, max_value=100, value=32)

height = st.number_input("Height (cm)", min_value=100, max_value=220, value=175)
weight = st.number_input("Weight (kg)", min_value=30, max_value=220, value=73)

# Compute BMI
bmi = weight / ((height / 100) ** 2)
st.caption(f"Calculated BMI: **{bmi:.1f}**")

smoker = st.selectbox("Do you smoke?", ["no", "yes"])
children = st.number_input("Number of dependants", min_value=0, max_value=15, value=1)

st.markdown("---")

# -----------------------------
# Helpers for user-friendly insight text
# -----------------------------
def bmi_message(bmi_value: float) -> str:
    if bmi_value >= 30:
        return "• Higher BMI is associated with increased insurance costs."
    elif bmi_value >= 25:
        return "• BMI moderately increases insurance cost."
    else:
        return "• Healthy BMI helps reduce insurance cost."

def age_message(age_value: int) -> str:
    if age_value >= 50:
        return "• Insurance costs tend to increase gradually with age."
    return "• Age has a moderate effect on insurance cost."

def children_message(children_value: int) -> str:
    if children_value >= 2:
        return "• More dependants moderately increase insurance cost."
    return "• Dependants have a small impact on cost."

def smoker_message(smoker_value: str) -> str:
    if smoker_value == "yes":
        return "• Smoking is the strongest factor increasing your estimated cost."
    return "• Not smoking helps keep your estimated cost lower."

# -----------------------------
# Predict
# -----------------------------
if st.button("Estimate Cost"):
    # Keep sex/region out of the UI for simplicity, but required by the trained model.
    # We set stable defaults to avoid confusing users.
    sex = "male"
    region = "northeast"

    input_df = pd.DataFrame([{
        "age": age,
        "bmi": bmi,
        "children": children,
        "sex": sex,
        "smoker": smoker,
        "region": region
    }])

    prediction = float(model.predict(input_df)[0])

    # Show a range (reduces false certainty). Keep it simple and readable.
    low = prediction * 0.85
    high = prediction * 1.15

    st.subheader("Estimated Annual Insurance Cost")
    st.metric("Estimate (KES)", f"{prediction:,.0f}")
    st.write(f"Likely range (KES): **{low:,.0f} – {high:,.0f}**")

    st.markdown("### What influences this estimate")
    st.write(smoker_message(smoker))
    st.write(bmi_message(bmi))
    st.write(age_message(age))
    st.write(children_message(children))

    st.markdown("---")
    st.caption(
        "Caution: This tool provides **estimates for awareness** and shows how different metrics may influence cost. "
        "Final insurance pricing is determined by **licensed/approved insurers** in line with regulatory guidelines."
    )
