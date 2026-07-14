import streamlit as st
import google.generativeai as genai

# حط الـ Key هنا مباشرة
MY_API_KEY = "AQ.Ab8RN6JcGvlFtN8yLnGhVjLzABMWszZOOnh6wyUwUUSB5Xmlpg"

st.set_page_config(page_title="Talabat QA Tool", layout="centered")
st.title("Talabat QA Analysis Engine")

chat_input = st.text_area("Paste Chat Transcript Here:", height=200)

if st.button("Generate Analysis"):
    if chat_input:
        try:
            genai.configure(api_key=MY_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
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
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste the chat transcript.")
