from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question)
    return response


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input", key="Input")
submit = st.button("Ask Me")

if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response Is:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("bot", chunk.text))

    st.subheader("History")

    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
