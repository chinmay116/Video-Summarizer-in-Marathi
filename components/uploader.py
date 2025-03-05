import streamlit as st


def render_uploader():
    """Render file upload and YouTube URL input"""
    upload_type = st.radio(
        "Choose upload method:",
        ["Upload Video", "YouTube URL"]
    )

    if upload_type == "Upload Video":
        return st.file_uploader(
            "Upload your video",
            type=["mp4", "webm", "avi"],
            help="Drag and drop your video file here"
        ), None
    else:
        return None, st.text_input(
            "Enter YouTube URL",
            placeholder="https://www.youtube.com/watch?v=..."
        )