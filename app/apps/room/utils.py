from uuid import uuid4
import shutil

from app.core.config.settings import app_settings


def save_file(file):
    with open(f"{app_settings.MEDIA_FOLDER}/{file.filename}", "wb") as image:
        shutil.copyfileobj(file.file, image)

    return f"{app_settings.MEDIA_FOLDER}/{file.filename}"

def create_filename(file):
    extension = file.split(".")[-1]
    return f"{uuid4()}.{extension}"