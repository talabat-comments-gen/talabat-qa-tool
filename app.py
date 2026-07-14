import streamlit as st
from openai import OpenAI

# Page settings
st.set_page_config(page_title="Talabat QA Engine", layout="centered")
st.title("🚀 Talabat QA Analysis Engine")

# Load OpenAI API Key
try:
    api_key = st.secrets["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"]
    client = OpenAI(api_key=api_key)
except Exception as e:
    st.error("Error: Please add OPENAI_API_KEY to Streamlit Secrets.")
    st.stop()

# Text area
chat_input = st.text_area("Paste Chat Transcript Here:", height=400)

if st.button("Generate Analysis"):
    if chat_input:
        with st.spinner('Analyzing with ChatGPT...'):
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
                
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3
                )
                
                st.success("Analysis Complete!")
                st.markdown("### 📝 Result:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"ChatGPT API Error: {e}")
    else:
        st.warning("Please paste the chat transcript first.")
