import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Reservoir Optimizer", layout="wide")

st.title("Intelligent AI-Based Reservoir Production Optimization")
st.caption("نظام ذكي متكامل يعتمد تقنيات الذكاء الاصطناعي لتحسين المكامن النفطية")

# تقسيم الصفحة
col1, col2 = st.columns([1,2])

# =========================
# SIDEBAR INPUT SECTION
# =========================
with col1:
    st.subheader("Project / Well Data")

    field_name = st.text_input("Field Name", "Field-Alpha-01")

    initial_pressure = st.slider("Initial Reservoir Pressure (psi)",
                                 1000, 5000, 2600)

    porosity = st.slider("Porosity (%)",
                         5.0, 35.0, 21.0)

    permeability = st.slider("Permeability (mD)",
                             10, 500, 150)

    oil_price = st.number_input("Oil Price per Barrel ($)",
                                min_value=10.0,
                                value=86.0)

    run = st.button("Run Optimization & AI Analysis")

# =========================
# MAIN OUTPUT SECTION
# =========================
with col2:

    if run:

        # Decline Curve Analysis (Exponential)
        months = np.arange(1, 13)
        qi = 650  # initial production rate
        decline_rate = 0.08 - (permeability / 10000)

        production = qi * np.exp(-decline_rate * months)

        # Annual Production
        annual_production = np.sum(production) * 30

        # Revenue
        revenue = annual_production * oil_price

        # Plot
        fig, ax = plt.subplots()
        ax.plot(months, production)
        ax.set_xlabel("Month")
        ax.set_ylabel("Rate (bbl/d)")
        ax.set_title(f"Production Forecast: {field_name}")

        st.pyplot(fig)

        colA, colB = st.columns(2)

        with colA:
            st.metric("Annual Oil Production (Barrels)",
                      f"{annual_production:,.0f}")

        with colB:
            st.metric("Estimated Annual Revenue ($)",
                      f"{revenue:,.0f}")

        # Simple AI Logic
        st.subheader("AI Recommendation")

        if porosity > 25 and permeability > 200:
            st.success("Reservoir quality is Excellent. Recommend aggressive production strategy.")
        elif porosity > 15:
            st.info("Reservoir quality is Moderate. Recommend controlled production.")
        else:
            st.warning("Low reservoir quality. Consider stimulation or EOR method.")
