
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)


# ---------------- MODEL ----------------

model = init_chat_model(
    "google_genai:gemini-3.5-flash-lite",
    max_output_tokens=200
)


# ---------------- PROMPT TEMPLATE ----------------

prompt_template = ChatPromptTemplate.from_messages([
    ("system", """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it in a clean readable format.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing -> write NULL
- Keep summary short (2-3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:

Short Summary:
"""),

    ("human", """
Extract information from this paragraph:

{paragraph}
""")
])


# ---------------- STREAMLIT UI ----------------

st.title("🎬 Movie Information Extractor")

st.write(
    "Enter a movie paragraph below to extract structured information."
)

para = st.text_area(
    "Movie Paragraph",
    placeholder="Paste your movie paragraph here...",
    height=200
)


# ---------------- EXTRACTION ----------------

if st.button("Extract Information", type="primary"):

    if para.strip():

        with st.spinner("Extracting movie information..."):

            try:
                final_prompt = prompt_template.invoke({
                    "paragraph": para
                })

                response = model.invoke(final_prompt)

                if isinstance(response.content, str):
                    result = response.content
                else:
                    result = "".join(
                        block.get("text", "")
                        for block in response.content
                        if isinstance(block, dict)
                        and block.get("type") == "text"
                    )

                st.subheader("Extracted Movie Information")
                st.markdown(result)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a movie paragraph first.")
