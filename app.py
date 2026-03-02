import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Advanced AI Reservoir Optimizer", layout="wide")

st.title("Advanced Intelligent AI-Based Reservoir Optimization System")
st.caption("AI-Driven Production Forecasting, Revenue Optimization & Reservoir Decision Support")

col1, col2 = st.columns([1,2])

# ==============================
# INPUT SECTION
# ==============================
with col1:

    st.subheader("Reservoir & Economic Inputs")

    field_name = st.text_input("Field Name", "Field-Alpha-01")

    initial_pressure = st.slider("Initial Reservoir Pressure (psi)", 1000, 5000, 3000)
    porosity = st.slider("Porosity (%)", 5.0, 35.0, 20.0)
    permeability = st.slider("Permeability (mD)", 10, 500, 150)
    water_cut = st.slider("Water Cut (%)", 0.0, 80.0, 20.0)

    oil_price = st.number_input("Oil Price ($/bbl)", value=85.0)
    operating_cost = st.number_input("Operating Cost ($/year)", value=2000000.0)
    discount_rate = st.slider("Discount Rate (%)", 5.0, 20.0, 10.0)

    run = st.button("Run AI Optimization")

# ==============================
# MAIN SECTION
# ==============================
with col2:

    if run:

        # ---------------------------
        # 1️⃣ Decline Curve
        # ---------------------------
        months = np.arange(1, 25)
        qi = 700
        decline_rate = 0.07 - (permeability / 12000)

        production = qi * np.exp(-decline_rate * months)
        production = production * (1 - water_cut/100)

        fig, ax = plt.subplots()
        ax.plot(months, production)
        ax.set_xlabel("Month")
        ax.set_ylabel("Oil Rate (bbl/d)")
        ax.set_title(f"Production Forecast: {field_name}")
        st.pyplot(fig)

        # ---------------------------
        # 2️⃣ Annual Production
        # ---------------------------
        annual_production = np.sum(production[:12]) * 30

        revenue = annual_production * oil_price
        net_cash_flow = revenue - operating_cost

        # ---------------------------
        # 3️⃣ NPV Calculation
        # ---------------------------
        discount = discount_rate / 100
        npv = 0
        for year in range(1,6):
            npv += net_cash_flow / ((1 + discount) ** year)

        roi = (net_cash_flow / operating_cost) * 100

        colA, colB, colC = st.columns(3)

        colA.metric("Annual Production (bbl)", f"{annual_production:,.0f}")
        colB.metric("Estimated Revenue ($)", f"{revenue:,.0f}")
        colC.metric("NPV (5 Years) ($)", f"{npv:,.0f}")

        st.metric("ROI (%)", f"{roi:.2f}%")

        # ---------------------------
        # 4️⃣ Machine Learning Model
        # ---------------------------
        # Generate synthetic training data
        X = np.random.rand(200,3)
        y = (X[:,0]*500 + X[:,1]*300 + X[:,2]*200) + np.random.randn(200)*20

        model = RandomForestRegressor()
        model.fit(X,y)

        prediction = model.predict([[porosity/100,
                                     permeability/500,
                                     initial_pressure/5000]])

        st.subheader("AI Production Potential Score")
        st.success(f"Predicted Production Potential Index: {prediction[0]:.2f}")

        # ---------------------------
        # 5️⃣ Water Breakthrough Detection
        # ---------------------------
        if water_cut > 50:
            st.error("⚠ High Water Breakthrough Detected. Recommend Water Shut-off Treatment.")
        elif water_cut > 30:
            st.warning("Moderate Water Production. Monitor Closely.")
        else:
            st.success("Water Level Under Control.")

        # ---------------------------
        # 6️⃣ Smart Optimization Recommendation
        # ---------------------------
        st.subheader("AI Optimization Recommendation")
        if porosity > 25 and permeability > 250:
            st.success("Reservoir Quality Excellent. Recommend Increasing Production Rate.")
        elif npv > 0:
            st.info("Project Economically Viable. Maintain Controlled Production Strategy.")
        else:
            st.warning("Low Economic Performance. Consider EOR or Artificial Lift Optimization.")
