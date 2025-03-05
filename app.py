import streamlit as st
from utils.video_processor import process_video
from utils.transcript_processor import get_youtube_transcript
from utils.youtube_processor import get_video_id
from utils.translator import translate_text
from utils.validation import validate_video
from utils.summarizer import generate_summary
from components.header import render_header
from components.uploader import render_uploader
from components.language_selector import render_language_selector

st.set_page_config(
    page_title="Video Summarizer",
    page_icon="🎥",
    layout="centered"
)


def main():
    render_header()

    # File upload or YouTube URL
    uploaded_file, youtube_url = render_uploader()

    if uploaded_file or youtube_url:
        # Validate input
        if uploaded_file:
            error = validate_video(uploaded_file)
            if error:
                st.error(error)
                return

        # Language selection
        selected_language = render_language_selector()

        # Process button
        if st.button("Generate Summary", type="primary", use_container_width=True):
            with st.status("Processing...") as status:
                try:
                    if youtube_url:
                        # Process YouTube URL
                        status.update(label="Fetching video transcript...", state="running")
                        video_id = get_video_id(youtube_url)
                        transcript = get_youtube_transcript(video_id)

                        status.update(label="Generating summary...", state="running")
                        summary = generate_summary(transcript)
                    else:
                        # Process uploaded video
                        status.update(label="Processing video...", state="running")
                        progress_bar = st.progress(0)
                        summary = process_video(uploaded_file, progress_bar)

                    # Translate if needed
                    if selected_language != "en":
                        status.update(label="Translating...", state="running")
                        summary = translate_text(summary, selected_language)

                    status.update(label="Done!", state="complete")

                    # Display summary
                    st.subheader("Video Summary")
                    st.write(summary)

                except Exception as e:
                    status.update(label="Error occurred!", state="error")
                    st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()