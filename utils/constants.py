SUPPORTED_LANGUAGES = [
    {"code": "en", "name": "English"},
    {"code": "hi", "name": "Hindi"},
    {"code": "mr", "name": "Marathi"},
    {"code": "es", "name": "Spanish"},
    {"code": "fr", "name": "French"},
    {"code": "de", "name": "German"},
    {"code": "ja", "name": "Japanese"},
    {"code": "ko", "name": "Korean"},
    {"code": "zh", "name": "Chinese (Simplified)"}
]

# Map between display language codes and Google Translate codes
LANGUAGE_CODE_MAP = {
    "zh": "zh-CN",  # Chinese Simplified
    "mr": "mr",     # Marathi
    "hi": "hi",     # Hindi
    # Add more mappings if needed
}

VIDEO_MAX_SIZE = 100 * 1024 * 1024  # 100MB
SUPPORTED_FORMATS = ["video/mp4", "video/webm", "video/x-msvideo"]