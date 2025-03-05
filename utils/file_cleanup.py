import os
import shutil

def cleanup_temp_files(temp_dir):
    """Clean up temporary files and directories"""
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"Error cleaning up temporary files: {e}")