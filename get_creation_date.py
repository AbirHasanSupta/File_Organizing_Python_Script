import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import subprocess

def get_creation_date(file_path):
    try:
        if file_path.lower().endswith((".jpg", ".jpeg", ".png", ".tiff", ".heif")):
            image = Image.open(file_path)
            exif_data = image._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == "DateTimeOriginal":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")

        elif file_path.lower().endswith((".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv")):
            try:
                result = subprocess.run(
                    ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                     "format_tags=creation_time", "-of", "default=noprint_wrappers=1:nokey=1", file_path],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                )
                creation_time = result.stdout.strip()
                if creation_time:
                    return datetime.strptime(creation_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            except Exception as e:
                print(f"Could not retrieve metadata for {file_path}: {e}")

        if os.name == "nt":
            return datetime.fromtimestamp(os.path.getctime(file_path))
        else:
            stat = os.stat(file_path)
            return datetime.fromtimestamp(getattr(stat, "st_birthtime", stat.st_mtime))

    except Exception as e:
        print(f"Error retrieving creation date for {file_path}: {e}")

    return datetime.fromtimestamp(os.path.getmtime(file_path))
