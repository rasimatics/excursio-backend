from dotenv import dotenv_values
from .base import BaseSettings
from pydantic import DirectoryPath



class DevelopmentSettings(BaseSettings):
    config = dotenv_values(".env.dev") 
    
    root_path = config['ROOT_PATH']
    
    DEBUG: bool = True
    DB_URI = config['DB_URI']

    SECRET_KEY:str = config["SECRET_KEY"]
    ALGORITHM: str = config["ALGORITHM"]
    ACCESS_TOKEN_EXPIRE_MINUTES: int  = config["ACCESS_TOKEN_EXPIRE_MINUTES"]

    APP_LOG_FILE_PATH: DirectoryPath = config['APP_LOG_FILE_PATH']
    APP_LOG_FILE: str = config["APP_LOG_FILE"]
  