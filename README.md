
# CineSage – Movie Information Extractor

An AI-powered application that extracts structured
movie information from unstructured text using
Google Gemini, LangChain, and Streamlit.

## Features
- Movie paragraph input.
- AI-powered movie information extraction.
- Reusable prompt templates.
- Structured output covering:
  - Movie title
  - Release year
  - Genre
  - Director
  - Main cast
  - Setting and location
  - Plot and themes
  - Ratings
  - Notable features
  - Short summary
- Interactive Streamlit interface.

## Tech Stack
Python, Streamlit, LangChain, Google Gemini API.

## Setup
1. Clone the repository.
2. Install dependencies:
   pip install -r requirements.txt
3. Create a .env file with your GOOGLE_API_KEY.
4. Run:
   streamlit run UIcore.py
