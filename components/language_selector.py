import streamlit as st
from utils.constants import SUPPORTED_LANGUAGES

def render_language_selector():
    return st.selectbox(
        "Select Output Language",
        options=[lang["code"] for lang in SUPPORTED_LANGUAGES],
        format_func=lambda x: next(lang["name"] for lang in SUPPORTED_LANGUAGES if lang["code"] == x),
        index=0
    )