import streamlit as st
from langchain.llms import OpenAI

# Set the title of the app
st.title('LLM Response Generator')

# Sidebar input for API key
api_key = st.sidebar.text_input('Enter OpenAI API Key:', type='password')

# Function to generate responses using the language model
def fetch_response(query_text):
    language_model = OpenAI(temperature=0.7, api_key=api_key)
    response = language_model.generate(query_text)
    return response

# Main form for text input and submission
with st.form('input_form'):
    user_input = st.text_area('Enter your question:', 'What are the three key pieces of advice for learning how to code?')
    submit_button = st.form_submit_button('Generate Response')

    # API key validation and response generation
    if submit_button:
        if not api_key.startswith('sk-'):
            st.warning('Invalid API key. Please enter a valid OpenAI API key.', icon='⚠️')
        else:
            generated_text = fetch_response(user_input)
            st.info(generated_text)
