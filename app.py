import streamlit as st
import google.generativeai as genai

# حط الـ API Key بتاعك هنا بين علامات التنصيص
MY_API_KEY = "AQ.Ab8RN6JakCWvc-3KfbBBM0Wxi8E3mM78HahWGndMe4LBE-pjww"

st.set_page_config(page_title="Talabat QA Tool", layout="centered")
st.title("Talabat QA Analysis Engine")

# شيلنا خانة الإدخال من الـ sidebar
chat_input = st.text_area("Paste Chat Transcript Here:", height=200)

if st.button("Generate Analysis"):
    if chat_input:
        try:
            genai.configure(api_key=MY_API_KEY)
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"""
            أنت Talabat Log Engine. استخرج الحقائق فقط بدون رأي أو تقييم.
            --- LOG ---
            (سجل الأحداث: CST, RST, Agent, RNA, FU مفصولة بـ //)
            --- CASE SUMMARY ---
            (ملخص موجز: المشكلة، الإجراء، النتيجة).
            الشات: {chat_input}
            """
            
            response = model.generate_content(prompt)
            st.markdown("### Result:")
            st.write(response.text)
        except Exception as e:
            st.error("خطأ في الاتصال، تأكد من الـ API Key.")
    else:
        st.warning("Please paste the chat transcript.")
