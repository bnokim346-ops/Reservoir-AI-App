import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Reservoir AI App", layout="wide")

st.title("🛢️ Reservoir Production Optimization")
st.write("تطبيق ذكي لتحسين إنتاج الآبار النفطية")

# المدخلات في الجانب
with st.sidebar:
    st.header("بيانات المكمن")
    pres = st.slider("الضغط (psi)", 1000, 5000, 3000)
    prm = st.number_input("النفاذية (mD)", 10, 1000, 150)

# حسابات بسيطة
time = np.arange(1, 13)
production = (pres * np.sqrt(prm) / 100) * np.exp(-0.05 * time)

# رسم بياني بسيط (بدون Plotly)
df = pd.DataFrame({'الشهر': time, 'الإنتاج': production})
st.subheader("مخطط الإنتاج المتوقع")
st.line_chart(df.set_index('الشهر'))

st.success(f"تم حساب التوقعات بنجاح لضغط {pres} psi")
