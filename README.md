# LLM Response Generator

This Streamlit application serves as a front end for generating responses using language models provided by OpenAI. It allows users to input a question and receive a generated response based on the input.

## Features

- **Secure API Key Input**: Users can enter their OpenAI API key securely in the sidebar. The input field hides the API key to protect user credentials.
- **Interactive Query Form**: Users can submit questions they want to be answered by the language model.
- **Response Generation**: Upon submitting a question, the app uses OpenAI's language model to generate and display a response.

## Setup and Installation

To run this application, you'll need to have Python and Streamlit installed. If you don't have Streamlit installed, you can install it via pip:

```bash
pip install streamlit
pip install langchain
```

## Running the App

To start the application, navigate to the project directory in your terminal and run:

```bash
streamlit run streamlit_app.py
```

## Deploying the App
To deploy the app to the streamlit Cloud, you need to follow these steps:
- Create a GitHub repository for the app, the repository should contain two files: **requiremnets.txt** and **streamlit_app**
- Go to Streamlit Community Cloud ([Link](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)), click the **New app** button from your workspace, then specify the repository, branch and main file path.
- Click the **Deploy** button

#### CONGRATULATIONS

## **Credit**
- **Source**: [Link](https://docs.streamlit.io/knowledge-base/tutorials/llm-quickstart)

