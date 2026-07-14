import streamlit as st
import google.generativeai as genai

# Page settings: Centered layout (less width)
st.set_page_config(page_title="Talabat QA Engine", layout="centered")
st.title("🚀 Talabat QA Analysis Engine")

# Safely load the API key from Secrets
try:
    api_key = st.secrets["AQ.Ab8RN6LsFrrH9br-ZSukEHjxRpkXapxYy4Y_ZX1PXWZHqJXosw"]
    genai.configure(api_key=api_key)
    # غيرنا الموديل هنا للموديل المستقر اللي مش بيعمل 404
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("Error: Please make sure GEMINI_API_KEY is added to Streamlit Secrets.")
    st.stop()

# Text area with increased height
chat_input = st.text_area("Paste Chat Transcript Here:", height=400)

if st.button("Generate Analysis"):
    if chat_input:
        with st.spinner('Analyzing...'):
            try:
                prompt = f"""
                You are the Talabat Log Engine. Extract FACTS ONLY from the chat transcript.
                Strictly follow this structure:
                --- LOG ---
                (CST: , RST: , Agent: , RNA: , FU: )
                --- CASE SUMMARY ---
                (Customer Issue, Action Taken, Final Result)
                
                Chat: {chat_input}
                """
                response = model.generate_content(prompt)
                st.success("Analysis Complete!")
                st.markdown("### 📝 Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"API Error: {e}")
    else:
        st.warning("Please paste the chat transcript first.")
