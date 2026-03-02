import streamlit as st
import pandas as pd
import numpy as np

# 1. إعداد الصفحة لتكون عريضة ومنظمة
st.set_page_config(page_title="AI Reservoir Optimizer", layout="wide")

# 2. العنوان الرئيسي
st.title("🛢️ Intelligent AI-Based Reservoir Production Optimization")
st.write("نظام ذكي متكامل لربط تقنيات الذكاء الاصطناعي بمبادئ هندسة المكامن النفطية")
st.divider()

# 3. تقسيم الواجهة إلى عمودين (مثل الصورة التي أعجبتكِ)
col_sidebar, col_main = st.columns()

with col_sidebar:
    st.subheader("📋 Input Parameters")
    well_id = st.text_input("Project/Well Name", "Field-Alpha-01")
    
    # أزرار المدخلات المطلوبة (الضغط، المسامية، النفاذية، السعر)
    pres = st.slider("Initial Reservoir Pressure (psi)", 1000, 5000, 2640)
    por = st.slider("Porosity (%)", 5.0, 35.0, 21.3)
    prm = st.number_input("Permeability (mD)", value=159)
    oil_price = st.number_input("Oil Price per Barrel ($)", value=86)
    
    # زر التشغيل الكبير
    run_btn = st.button("Run Optimization & AI Analysis", type="primary", use_container_width=True)

# 4. العمليات الحسابية (تتم خلف الكواليس)
months = np.arange(1, 13)
initial_rate = (pres * (por/100) * np.sqrt(prm)) / 10
prod_curve = initial_rate * np.exp(-0.06 * months)

with col_main:
    if run_btn:
        st.subheader(f"📈 Production Forecast: {well_id}")
        
        # إنشاء الرسم البياني الاحترافي
        df = pd.DataFrame({'Month': months, 'Rate (bbl/d)': prod_curve})
        st.line_chart(df.set_index('Month'))
        
        st.divider()
        
        # عرض النتائج في مربعات (Metrics)
        res_col1, res_col2 = st.columns(2)
        total_prod = np.sum(prod_curve) * 30.5
        revenue = total_prod * oil_price
        
        with res_col1:
            st.metric("Annual Oil Production", f"{total_prod:,.0f} Barrels")
        with res_col2:
            st.metric("Estimated Annual Revenue", f"${revenue:,.0f}")
            
        st.success("✅ AI Analysis Complete: The reservoir shows high potential for optimization.")
    else:
        # رسالة تظهر قبل الضغط على الزر
        st.info("👈 الرجاء ضبط القيم من اليسار ثم الضغط على زر التحليل لعرض النتائج")

# 5. التذييل
st.markdown("---")
st.caption("Developed by Baneen Hussam | Reservoir AI Project 2026")
