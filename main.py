import os
import streamlit as st
import textwrap
import google.generativeai as genai

# Set the API key directly
GOOGLE_API_KEY = "AIzaSyA9u1nGTGjVyAvWPjEt9tbXI1vzsqh935k"

# Configure the generative AI library
genai.configure(api_key=GOOGLE_API_KEY)

# Streamlit app setup
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

# Function to get Gemini response
def get_gemini_response(question):
    response = genai.generate_text(model='gemini-pro', prompt=question)
    return response.result

# App input and response
input_text = st.text_input("Input: ", key="input")
if st.button("Ask the question") and input_text:
    try:
        response = get_gemini_response(input_text)
        st.subheader("The Response is")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
