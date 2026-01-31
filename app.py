import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from ml_model import predict_risk_ml
from weather_api import get_rainfall
from flood_logic import calculate_flood_risk
from data_logger import log_data

# -----------------------------
# SESSION STATE
# -----------------------------
if "risk_score" not in st.session_state:
    st.session_state.risk_score = None

if "level" not in st.session_state:
    st.session_state.level = None

# -----------------------------
# PAGE SETUP
# -----------------------------
st.set_page_config(page_title="Flood Risk System", layout="centered")
st.title("🌊 Smart Flood Risk Prediction System")
st.caption(
    "AI-assisted flood risk awareness to support climate resilience and sustainable cities. This system supports climate resilience by enabling early flood risk awareness and preventive action."
)


# -----------------------------
# LOCATION DATA
# -----------------------------
locations = {
    "Thiruvananthapuram": (8.5241, 76.9366),
    "Kochi": (9.9312, 76.2673),
    "Kozhikode": (11.2588, 75.7804),
    "Thrissur": (10.5276, 76.2144),
    "Kollam": (8.8932, 76.6141),
    "Alappuzha": (9.4981, 76.3388),
    "Palakkad": (10.7867, 76.6548),
    "Malappuram": (11.0732, 76.0740),
    "Kannur": (11.8745, 75.3704),
    "Kasaragod": (12.4996, 74.9869),
    "Kottayam": (9.5916, 76.5222),
    "Pathanamthitta": (9.2648, 76.7870),
    "Idukki": (9.8497, 76.9720),
    "Wayanad": (11.6854, 76.1320)
}

# -----------------------------
# LOCATION SELECTOR
# -----------------------------
city = st.selectbox("📍 Select Location", locations.keys())
LAT, LON = locations[city]

map_df = pd.DataFrame({"lat": [LAT], "lon": [LON]})
st.map(map_df)

# -----------------------------
# RAINFALL INPUT
# -----------------------------
use_manual = st.checkbox("Use manual rainfall input")

if use_manual:
    rainfall = st.slider("🌧️ Manual Rainfall (mm/hour)", 0, 100, 10)
else:
    rainfall = get_rainfall(LAT, LON)

# -----------------------------
# DRAINAGE INPUT
# -----------------------------
drainage = st.selectbox(
    "🕳️ Drainage Condition",
    ["Good", "Average", "Poor"]
)

# -----------------------------
# ANALYSIS
# -----------------------------
if st.button("🚨 Analyze Flood Risk"):

    score, lvl = calculate_flood_risk(rainfall, drainage)

    st.session_state.risk_score = score
    st.session_state.level = lvl

    ml_risk = predict_risk_ml(rainfall)
    st.metric("🤖 ML Predicted Risk", round(ml_risk, 2))

 # Risk alerts
    if lvl == "LOW":
        st.success("🟢 LOW Flood Risk – Area is safe")
        st.info(" Recommendation: Normal conditions. Maintain drainage systems.")

    elif lvl == "MODERATE":
        st.warning("🟡 MODERATE Flood Risk – Stay alert")
        st.info(" Recommendation: Monitor rainfall and clear nearby drains.")

    else:
        st.error("🔴 HIGH Flood Risk – Immediate action required")
        st.info(" Recommendation: Avoid low-lying areas and ensure emergency drainage clearance.")
        st.caption("This alert would be sent to authorities and residents in the affected area.")

# -----------------------------
# DISPLAY + CHART
# -----------------------------
if st.session_state.risk_score is not None:

    st.metric(
        "Flood Risk Score",
        round(st.session_state.risk_score, 2)
    )

    fig, ax = plt.subplots()
    ax.plot(
        [0, 1],
        [0, st.session_state.risk_score],
        marker="o"
    )
    ax.set_title("Flood Risk Index")
    ax.set_ylim(0, 60)
    ax.grid(True)
    st.pyplot(fig)

st.markdown("**AI for Sustainability • Climate Adaptation • Disaster Risk Reduction**")

