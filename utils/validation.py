from .constants import VIDEO_MAX_SIZE, SUPPORTED_FORMATS


def validate_video(file):
    if not file:
        return "Please select a video file"

    if file.size > VIDEO_MAX_SIZE:
        return "File size must be less than 100MB"

    if file.type not in SUPPORTED_FORMATS:
        return "Unsupported video format. Please use MP4, WebM, or AVI"

    return None