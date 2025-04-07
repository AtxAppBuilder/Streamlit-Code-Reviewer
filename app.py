import streamlit as st
from pylint.lint import Run
from pylint.reporters.text import TextReporter
from io import StringIO
from openai import OpenAI
import os

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY") or "your-openai-api-key"
client = OpenAI(api_key=openai_api_key)

# App configuration
st.set_page_config(page_title="AI Code Reviewer Portfolio", page_icon="💻", layout="wide")

# Sidebar for portfolio branding
with st.sidebar:
    st.header("About Me")
    st.write("Hi! I'm [Joe], a Python enthusiast building AI-powered tools. This app showcases my skills in Streamlit, OpenAI, and code analysis.")
    st.write("Check out my [GitHub](https://github.com/AtxAppBuilder) or [LinkedIn](https://www.linkedin.com/in/joseph-killelea-31b3a14b/)!")

# Main app
st.title("AI-Powered Code Reviewer")
st.markdown("Paste your Python code below, and I'll review it with static analysis and AI insights!")

# Code input
st.header("Submit Your Code")
code_input = st.text_area("Enter Python code here", height=300, placeholder="e.g., def hello(): print('Hello, World!')")
submit_button = st.button("Review Code")

if submit_button and code_input:
    # Save code to a temp file for analysis
    with open("temp_code.py", "w") as f:
        f.write(code_input)

    # Tabs for different review types
    tab1, tab2, tab3 = st.tabs(["Static Analysis", "AI Feedback", "Download Report"])

    with tab1:
        # Static Analysis with Pylint
        st.subheader("Static Analysis (Pylint)")
        output = StringIO()
        reporter = TextReporter(output)
        try:
            Run(["temp_code.py"], reporter=reporter, exit=False)
            pylint_results = output.getvalue()
            st.code(pylint_results, language="text")
        except Exception as e:
            st.error(f"Error running Pylint: {e}")

    with tab2:
        st.subheader("AI-Powered Feedback")
        prompt = """
        Review this Python code and provide detailed feedback on:
        - Code quality (readability, structure, naming)
        - Potential bugs or logical errors
        - Suggestions for improvement (best practices, optimization)

        Code:
        ```python
        """
        {code_input}

        st.markdown("---")
        st.write("Built by Joe Killelea using Streamlit and OpenAI | © 2025")