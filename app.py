import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="أداة تحليل طلبات", layout="centered")
st.title("🚀 أداة تحليل تقارير الجودة")

# محاولة سحب المفتاح
try:
    # الكود هنا بيدور على اسم "GEMINI_API_KEY"
    api_key = st.secrets["AQ.Ab8RN6Ix2qeVMs0rWW9B2pwjubJ21C-XVGnjthFWnoliFv2eSQ"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    chat_input = st.text_area("انسخ هنا نص الشات (Transcript):", height=400)

    if st.button("بدء التحليل"):
        if chat_input:
            with st.spinner('جاري التحليل...'):
                prompt = f"حلل الشات التالي: {chat_input}"
                response = model.generate_content(prompt)
                st.write(response.text)
        else:
            st.warning("من فضلك ضع نص الشات.")

except Exception as e:
    st.error(f"⚠️ خطأ في السيكريتس: {e}")
    st.write("تأكد أن الاسم في إعدادات Secrets هو: **GEMINI_API_KEY**")
