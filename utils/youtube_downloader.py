import tempfile
import os
from pytube import YouTube
import time
from urllib.error import HTTPError


def download_youtube_video(url, progress_bar=None):
    """Download YouTube video with retries and proper error handling"""
    max_retries = 3
    retry_delay = 2

    for attempt in range(max_retries):
        try:
            # Configure YouTube object with custom options
            yt = YouTube(
                url,
                on_progress_callback=lambda stream, chunk, bytes_remaining:
                progress_bar.progress(int((1 - bytes_remaining / stream.filesize) * 100))
                if progress_bar else None,
                use_oauth=False,
                allow_oauth_cache=True
            )

            # Get highest quality mp4 stream
            video = yt.streams.filter(
                progressive=True,
                file_extension='mp4'
            ).order_by('resolution').desc().first()

            if not video:
                raise Exception("No suitable video stream found")

            # Create temp directory and download
            temp_dir = tempfile.mkdtemp()
            video_path = os.path.join(temp_dir, "youtube_video.mp4")

            # Download with progress tracking
            if progress_bar:
                progress_bar.progress(0)

            video.download(output_path=temp_dir, filename="youtube_video.mp4")

            if progress_bar:
                progress_bar.progress(100)

            return video_path, temp_dir

        except HTTPError as e:
            if e.code == 403 and attempt < max_retries - 1:
                time.sleep(retry_delay * (attempt + 1))  # Exponential backoff
                continue
            raise Exception(f"YouTube access forbidden. Please try again later or use direct video upload.")

        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay * (attempt + 1))
                continue
            raise Exception(f"Error downloading YouTube video: {str(e)}")

    raise Exception("Failed to download video after multiple attempts")