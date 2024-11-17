import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input", key="Input")
submit = st.button("Ask the Question")

if submit:
    response = get_gemini_response(input)
    st.subheader("Response is")
    # st.write(response.candidates[0].content.parts[0])
    st.write(response)
