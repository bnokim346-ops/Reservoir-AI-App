import streamlit as st
import pandas as pd
import numpy as np

# إعدادات الصفحة لتكون عريضة واحترافية
st.set_page_config(page_title="Intelligent AI Reservoir App", layout="wide")

# العنوان الرئيسي ووصف النظام
st.title("🛢️ Intelligent AI-Based Reservoir Production Optimization")
st.markdown("---")

# تقسيم الصفحة إلى جزئين: يسار للمدخلات ويمين للنتائج


with col_inputs:
    st.subheader("📋 Input Parameters")
    
    # حقل لاسم البئر
    well_name = st.text_input("Project/Well Name", "Field-Alpha-01")
    
    # أشرطة التحكم (Sliders) للمسامية والضغط
    pres = st.slider("Initial Reservoir Pressure (psi)", 1000, 5000, 2640)
    por = st.slider("Porosity (%)", 5.0, 35.0, 21.3)
    
    # حقول إدخال رقمية للنفاذية والسعر
    prm = st.number_input("Permeability (mD)", value=159)
    oil_price = st.number_input("Oil Price per Barrel ($)", value=86)
    
    # زر التشغيل (مثل الموجود في الصورة)
    run_btn = st.button("Run Optimization & AI Analysis", type="primary", use_container_width=True)

# الحسابات الهندسية
time = np.arange(1, 13)
# معادلة Decline Curve مبسطة تعتمد على مدخلاتكِ
initial_rate = (pres * (por/100) * np.sqrt(prm)) / 10
production = initial_rate * np.exp(-0.06 * time)

with col_display:
    if run_btn:
        st.subheader(f"📈 Production Forecast: {well_name}")
        
        # إنشاء الرسم البياني
        chart_data = pd.DataFrame({
            'Month': time,
            'Rate (bbl/d)': production
        }).set_index('Month')
        
        st.line_chart(chart_data)
        
        st.markdown("---")
        
        # عرض النتائج الرقمية (Metrics) بشكل أفقي مركب
        m1, m2 = st.columns(2)
        
        total_annual = np.sum(production) * 30.5
        annual_revenue = total_annual * oil_price
        
        with m1:
            st.metric("Annual Oil Production", f"{total_annual:,.0f} Barrels")
        with m2:
            st.metric("Estimated Annual Revenue", f"${annual_revenue:,.0f}")
            
        st.info("💡 AI Insight: Current parameters suggest stable production with 5% monthly decline.")
    else:
        st.warning("👈 Please adjust parameters and click 'Run Optimization' to see results.")

# تذييل الصفحة
st.markdown("---")
st.caption("Developed for Reservoir Engineering AI Competition | 2026")
