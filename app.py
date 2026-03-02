import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Reservoir App", layout="wide")

st.title("AI Reservoir Production Forecast")

col1, col2 = st.columns([1,2])

# =====================
# INPUTS
# =====================
with col1:

    st.subheader("Enter Reservoir Data")

    porosity = st.number_input("Porosity (%)", min_value=1.0, max_value=40.0, value=20.0)
    permeability = st.number_input("Permeability (mD)", min_value=1.0, value=150.0)
    pressure = st.number_input("Reservoir Pressure (psi)", min_value=500.0, value=3000.0)
    oil_price = st.number_input("Oil Price ($/bbl)", min_value=10.0, value=80.0)

    run = st.button("Run Calculation")

# =====================
# OUTPUT
# =====================
with col2:

    if run:

        months = np.arange(1,13)

        # معادلة بسيطة تعتمد على القيم المدخلة
        base_rate = (porosity * 2) + (permeability * 0.5) + (pressure / 100)

        decline = 0.08
        production = base_rate * np.exp(-decline * months)

        df = pd.DataFrame({
            "Month": months,
            "Production (bbl/day)": production
        })

        st.subheader("Production Forecast")
        st.line_chart(df.set_index("Month"))

        annual_production = production.sum() * 30
        revenue = annual_production * oil_price

        st.success("Results")

        st.write("Annual Production (barrels):", round(annual_production,0))
        st.write("Estimated Revenue ($):", round(revenue,0))
