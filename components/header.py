import streamlit as st


def render_header():
    st.title("🎥 Video Summarizer")
    st.markdown("""
        Upload your video and get an instant summary in your preferred language.

        Supported formats: MP4, WebM, AVI | Max size: 100MB
    """)