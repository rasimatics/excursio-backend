from pathlib import Path

from pydantic import BaseSettings as Settings


current_file = Path(__file__)
current_file_dir = current_file.parent

project_root = current_file_dir.parent
project_root_absolute = project_root.resolve()

BASE_DIR = project_root_absolute.parent.parent


class BaseSettings(Settings):
    title: str = "Backend"
    version: str = "1.0.0"
    description: str = "Backend"
    docs_url: str = "/docs"
    
    PREFIX: str = ""
    MEDIA_FOLDER: str = "media"