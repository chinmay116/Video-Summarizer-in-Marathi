import whisper_timestamped as whisper


def transcribe_audio(audio_path):
    """Transcribe audio to text using Whisper"""
    # Load model
    model = whisper.load_model("base")

    # Transcribe
    result = whisper.transcribe(
        model,
        audio_path,
        language="auto"  # Can be auto-detected or specified
    )

    # Extract full text
    return " ".join([segment["text"] for segment in result["segments"]])