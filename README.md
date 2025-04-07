# Streamlit AI Code Reviewer 💻

![Streamlit AI Code Reviewer](https://img.shields.io/badge/Status-Active-brightgreen)  
A Streamlit web app that provides automated code reviews for Python code using static analysis and AI-powered feedback, built to streamline the code review process for developers.

## Overview

The **Streamlit AI Code Reviewer** is a web application designed to help developers improve their Python code through automated feedback. Built with Streamlit and powered by the OpenAI API, the app allows users to input their code, receive static analysis from Pylint, and get detailed AI-powered feedback on code quality, potential bugs, and best practices. The app features an interactive UI with tabs for different types of feedback and a sidebar showcasing my portfolio as a software engineering enthusiast.

This project demonstrates my skills in Python, Streamlit, API integration, and secure environment management, making it a key part of my portfolio for showcasing AI-driven tools.

## Features

- **Interactive UI**: Input Python code via a Streamlit text area and view feedback through an intuitive interface with tabs for Static Analysis, AI Feedback, and Download Report.
- **Static Code Analysis**: Analyze code quality using Pylint, displaying detailed reports on potential issues and style violations.
- **AI-Powered Feedback**: Leverage the OpenAI API to provide in-depth feedback on code readability, structure, naming, potential bugs, and suggestions for improvement.
- **Secure API Key Management**: Safely manage the OpenAI API key using environment variables and `python-dotenv`.
- **Portfolio Branding**: Includes a sidebar with links to my GitHub and LinkedIn profiles, highlighting my work as a developer.

## Tech Stack

- **Framework**: Streamlit
- **Backend**: Python
- **AI Integration**: OpenAI API
- **Static Analysis**: Pylint
- **Environment Management**: python-dotenv
- **Standard Libraries**: `io`, `os`

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- [Python](https://www.python.org/) (v3.8 or higher)
- [Git](https://git-scm.com/)
- An [OpenAI API key](https://platform.openai.com/api-keys) for AI-powered feedback

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AtxAppBuilder/Streamlit-Code-Reviewer.git
   cd Streamlit-Code-Reviewer
