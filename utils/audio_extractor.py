from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_path):
    """Extract audio from video file"""
    with VideoFileClip(video_path) as video:
        video.audio.write_audiofile(
            audio_path,
            fps=16000,  # Whisper expects 16kHz
            nbytes=2,   # 16-bit
            codec='pcm_s16le'  # WAV format
        )