import streamlit as st
import google.generativeai as genai

# اسحب المفتاح من الـ Secrets
api_key = st.secrets["AQ.Ab8RN6JakCWvc-3KfbBBM0Wxi8E3mM78HahWGndMe4LBE-pjww"]

# تحديث الإعدادات
genai.configure(api_key=api_key)

# نستخدم نسخة الموديل الأكثر توافقاً حالياً
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Talabat QA Analysis Engine")
chat_input = st.text_area("Paste Chat Transcript Here:", height=200)

if st.button("Generate Analysis"):
    if chat_input:
        try:
            response = model.generate_content(chat_input + "\n\nاستخرج الحقائق فقط (CST, RST, Agent, RNA, FU) وملخص للمشكلة.")
            st.markdown("### Result:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
