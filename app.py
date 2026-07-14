import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Talabat QA Tool", layout="centered")
st.title("Talabat QA Analysis Engine")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
chat_input = st.text_area("Paste Chat Transcript Here:", height=200)

if st.button("Generate Analysis"):
    if api_key and chat_input:
        genai.configure(api_key=api_key)
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
    else:
        st.warning("Please enter API Key and Chat Transcript.")import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Talabat QA Tool", layout="centered")
st.title("Talabat QA Analysis Engine")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
chat_input = st.text_area("Paste Chat Transcript Here:", height=200)

if st.button("Generate Analysis"):
    if api_key and chat_input:
        genai.configure(api_key=api_key)
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
    else:
        st.warning("Please enter API Key and Chat Transcript.")import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Talabat QA Tool", layout="centered")
st.title("Talabat QA Analysis Engine")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
chat_input = st.text_area("Paste Chat Transcript Here:", height=200)

if st.button("Generate Analysis"):
    if api_key and chat_input:
        genai.configure(api_key=api_key)
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
    else:
        st.warning("Please enter API Key and Chat Transcript.")