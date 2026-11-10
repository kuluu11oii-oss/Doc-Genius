import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load the .env file
load_dotenv()

# Retrieve the API key from the environment variable
GEMINI_API = os.getenv("GEMINI_API")
client=genai.Client(api_key=GEMINI_API)

# Streamlit app
st.title("Gemini AI Content Generator")

# Text input for user prompt (with form submission on Enter)
user_input = st.text_input("Enter a prompt:")

# Check if user input is provided and the 'Enter' key is pressed
if user_input:
    # Use the Gemini model to generate content
    response = client.models.generate_content(model="gemini-2.5-flash",contents=user_input)

    # Display the generated response
    st.write("Response from Gemini AI:")
    st.write(response.text)
else:
    st.write("Please enter a prompt to generate content.")