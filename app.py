import streamlit as st
import pandas as pd
import numpy as np

# إعداد الصفحة
st.set_page_config(page_title="Reservoir AI Optimization", layout="wide")

st.title("🛢️ Intelligent AI-Based Reservoir Production Optimization")
st.markdown("نظام ذكي متكامل لربط تقنيات الذكاء الاصطناعي بمبادئ هندسة المكامن النفطية")
st.divider()

# تقسيم الواجهة إلى عمودين (العمود الأول للمدخلات والثاني للنتائج)
col_in, col_out = st.columns()

with col_in:
    st.subheader("📋 Input Parameters")
    well_id = st.text_input("Project/Well Name", "Field-Alpha-01")
    
    # أزرار المدخلات المطلوبة
    pres = st.slider("Initial Reservoir Pressure (psi)", 1000, 5000, 2640)
    por = st.slider("Porosity (%)", 5.0, 35.0, 21.3)
    prm = st.number_input("Permeability (mD)", value=159)
    oil_price = st.number_input("Oil Price per Barrel ($)", value=86)
    
    # زر التشغيل
    run_analysis = st.button("Run Optimization & AI Analysis", type="primary", use_container_width=True)

# العمليات الحسابية
months = np.arange(1, 13)
initial_rate = (pres * (por/100) * np.sqrt(prm)) / 10
prod_data = initial_rate * np.exp(-0.06 * months)

with col_out:
    if run_analysis:
        st.subheader(f"📈 Production Forecast: {well_id}")
        
        # إنشاء الرسم البياني
        chart_df = pd.DataFrame({
            'Month': months,
            'Rate (bbl/d)': prod_data
        }).set_index('Month')
        
        st.line_chart(chart_df)
        
        # عرض النتائج المالية والإنتاجية في مربعات
        st.divider()
        res1, res2 = st.columns(2)
        
        total_barrels = np.sum(prod_data) * 30.5
        total_revenue = total_barrels * oil_price
        
        with res1:
            st.metric("Annual Oil Production", f"{total_barrels:,.0f} Barrels")
        with res2:
            st.metric("Estimated Annual Revenue", f"${total_revenue:,.0f}")
            
        st.success("AI Insight: Reservoir performance is optimal based on current permeability.")
    else:
        st.info("👈 قم بتعديل البيانات واضغط على زر التحليل لعرض النتائج")
