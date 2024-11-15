import streamlit as st
import os
import textwrap
import google.generativeai as genai

# Set the API key directly
GOOGLE_API_KEY = "AIzaSyA9u1nGTGjVyAvWPjEt9tbXI1vzsqh935k"

# Configure the generative AI library
genai.configure(api_key=GOOGLE_API_KEY)

# Function to format text into Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Function to load OpenAI model and get response
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Flavours Fusion Application")

# Input text from the user
input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If the "Ask" button is clicked
if submit and input_text:
    try:
        response = get_gemini_response(input_text)
        st.subheader("The Response is")
        st.write(to_markdown(response))
    except Exception as e:
        st.error(f"An error occurred: {e}")
