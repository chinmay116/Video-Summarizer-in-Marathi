import os
import tempfile
from moviepy.editor import VideoFileClip
from .audio_extractor import extract_audio
from .speech_to_text import transcribe_audio
from .summarizer import generate_summary
from .file_cleanup import cleanup_temp_files


def process_video(video_file, progress_bar):
    """Process video through multiple stages: audio extraction, transcription, and summarization"""
    try:
        # Create temp directory
        temp_dir = tempfile.mkdtemp()
        video_path = os.path.join(temp_dir, "input_video.mp4")
        audio_path = os.path.join(temp_dir, "extracted_audio.wav")

        # Save uploaded file
        with open(video_path, "wb") as f:
            f.write(video_file.getvalue())

        # Update progress
        progress_bar.progress(10)

        # Extract audio

        extract_audio(video_path, audio_path)
        progress_bar.progress(30)

        # Transcribe audio
        transcription = transcribe_audio(audio_path)
        progress_bar.progress(70)

        # Generate summary
        summary = generate_summary(transcription)
        progress_bar.progress(100)

        return summary

    finally:
        # Cleanup temporary files
        cleanup_temp_files(temp_dir)