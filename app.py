import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="أداة تحليل طلبات", layout="centered")
st.title("🚀 أداة تحليل تقارير الجودة")

# هذا السطر هو الوحيد الذي يقرأ من الـ Secrets
# تأكد ألا تضع أي مفاتيح داخل الكود هنا
try:
    api_key = st.secrets["AQ.Ab8RN6Ix2qeVMs0rWW9B2pwjubJ21C-XVGnjthFWnoliFv2eSQ"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("الرجاء مراجعة إعدادات Secrets.")
    st.stop()

chat_input = st.text_area("انسخ هنا نص الشات:", height=400)

if st.button("بدء التحليل"):
    if chat_input:
        with st.spinner('جاري التحليل...'):
            response = model.generate_content("حلل الشات التالي: " + chat_input)
            st.write(response.text)
    else:
        st.warning("يرجى إدخال الشات.")
