import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)

    return response.text


st.set_page_config(page_title="Gemini Image Vision Demo")
st.header("Gemini Application")
input = st.text_input("Input", key="Input")
fileupload = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])
image = ""
if fileupload is not None:
    image = Image.open(fileupload)
    st.image(image, caption="Upload an Image", use_column_width=True)

submit = st.button("Tell me about Image")

if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response Is")
    st.write(response)
