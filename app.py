import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Reservoir AI Optimizer", layout="wide")

st.title("🛢️ Intelligent AI-Based Reservoir Production Optimization")
st.write("نظام ذكي لتحسين إنتاج المكامن النفطية والكشف المبكر عن اختراق المياه")

# المدخلات
with st.sidebar:
    st.header("📊 Reservoir Parameters")
    name = st.text_input("Well Name", "Well-01")
    pres = st.slider("Pressure (psi)", 1000, 5000, 3000)
    por = st.slider("Porosity (%)", 5, 35, 20)
    prm = st.number_input("Permeability (mD)", 10, 1000, 150)
    price = st.number_input("Oil Price ($)", 40, 120, 80)

# الحسابات الهندسية
time = np.arange(1, 13)
initial_rate = (pres * (por/100) * np.sqrt(prm)) / 10
production = initial_rate * np.exp(-0.05 * time)

# العرض
col1, col2 = st.columns()

with col1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=production, mode='lines+markers', name='Oil Rate'))
    fig.update_layout(title="Annual Production Forecast", xaxis_title="Month", yaxis_title="bbl/d")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🤖 AI Insights")
    risk = (pres / 5000) * (prm / 1000) * 100
    if risk > 70:
        st.error(f"High Water Risk: {risk:.1f}%")
    else:
        st.success(f"Safe Zone: {risk:.1f}%")
    
    rev = np.sum(production) * 30 * price
    st.metric("Expected Revenue", f"${rev:,.0f}")

st.info("💡 Engineering Note: Pressure maintenance is key for this well's longevity.")
