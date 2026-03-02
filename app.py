import streamlit as st

st.set_page_config(page_title="AI Reservoir Calculator", layout="wide")

st.title("Intelligent AI-Based Reservoir Production Optimization")

st.write("Enter reservoir properties to estimate porosity, permeability, pressure and oil value.")

# تقسيم الصفحة الى عمودين (هنا التصحيح)
col1, col2 = st.columns(2)

with col1:
    st.header("Input Data")

    bulk_volume = st.number_input("Bulk Volume (m3)", min_value=0.0, value=1000.0)
    pore_volume = st.number_input("Pore Volume (m3)", min_value=0.0, value=200.0)
    flow_rate = st.number_input("Flow Rate (m3/day)", min_value=0.0, value=150.0)
    viscosity = st.number_input("Oil Viscosity (cp)", min_value=0.1, value=1.0)
    area = st.number_input("Area (m2)", min_value=0.1, value=50.0)
    length = st.number_input("Length (m)", min_value=0.1, value=10.0)
    oil_price = st.number_input("Oil Price ($/barrel)", min_value=1.0, value=70.0)
    oil_volume_barrels = st.number_input("Oil Volume (barrels)", min_value=0.0, value=10000.0)

    calculate = st.button("Calculate")

with col2:
    st.header("Results")

    if calculate:

        # 1️⃣ Porosity
        if bulk_volume > 0:
            porosity = pore_volume / bulk_volume
        else:
            porosity = 0

        # 2️⃣ Permeability (Darcy approximation)
        if area * viscosity > 0:
            permeability = (flow_rate * viscosity * length) / area
        else:
            permeability = 0

        # 3️⃣ Reservoir Pressure (simplified estimation)
        pressure = flow_rate * viscosity * 10  # تبسيط لغرض المشروع

        # 4️⃣ Oil Value
        oil_value = oil_price * oil_volume_barrels

        st.success("Calculation Completed Successfully ✅")

        st.write(f"Porosity: {porosity:.4f}")
        st.write(f"Permeability: {permeability:.4f} mD (approx)")
        st.write(f"Estimated Reservoir Pressure: {pressure:.2f} psi (approx)")
        st.write(f"Estimated Oil Value: ${oil_value:,.2f}")
