import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Senior Reservoir AI", layout="wide")

# تصميم الواجهة (Dark Mode Style)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e4253; }
    </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية للمدخلات
st.sidebar.header("🛠 Well Parameters")
well_name = st.sidebar.text_input("Well Name", "Bnokim-01")
pressure = st.sidebar.slider("Reservoir Pressure (psi)", 1000, 5000, 3200)
porosity = st.sidebar.slider("Porosity (%)", 5, 35, 18)
water_cut = st.sidebar.slider("Water Cut (%)", 0, 100, 25)
oil_price = st.sidebar.number_input("Oil Price ($/bbl)", value=75)

# الحسابات الهندسية والاقتصادية (الذكاء الاصطناعي)
npv = (pressure * porosity * 100) / (water_cut + 1) * (oil_price / 100)
payback = 120 / (oil_price * 0.5) if water_cut < 50 else 240 / (oil_price * 0.2)

# عرض النتائج الكبيرة (KPIs)
st.title(f"📊 {well_name}: Executive Analysis")
col1, col2, col3 = st.columns(3)
col1.metric("Project NPV", f"${npv:,.0f}", "+12%")
col2.metric("Payback Period", f"{payback:.1f} Months", "-2 Months")
col3.metric("Reservoir Health", "Stable" if water_cut < 40 else "Critical", None)

# الرسوم البيانية (Production Forecast)
st.subheader("📈 Production Forecasting (12 Months)")
months = np.arange(1, 13)
rate = [1000 * np.exp(-0.05 * m) for m in months]
cum = np.cumsum(rate)

fig = go.Figure()
fig.add_trace(go.Scatter(x=months, y=rate, name="Oil Rate (bopd)", line=dict(color='#00f2ff', width=3)))
fig.add_trace(go.Scatter(x=months, y=cum, name="Cumulative (bbl)", yaxis="y2", line=dict(color='#ff9900', dash='dash')))

fig.update_layout(
    yaxis=dict(title="Production Rate"),
    yaxis2=dict(title="Cumulative", overlaying="y", side="right"),
    template="plotly_dark",
    legend=dict(orientation="h", y=1.1)
)
st.plotly_chart(fig, use_container_width=True)

# التوصيات الهندسية (الخبير الاستشاري)
st.subheader("🤖 Strategic Field Plan")
if water_cut > 40:
    st.error("⚠️ Warning: High Water Cut detected. Recommendation: Initiate ESP or Gas Lift installation.")
if pressure < 2500:
    st.warning("📉 Pressure Depletion: Consider Water Injection or Pressure Maintenance protocols.")
if water_cut <= 40 and pressure >= 2500:
    st.success("✅ Optimum Production: Maintain current choke settings. No intervention required.")

st.info("AI Insights: This well shows high potential for Enhanced Oil Recovery (EOR) in Q4.")