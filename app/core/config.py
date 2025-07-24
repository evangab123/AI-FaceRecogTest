import os
from dotenv import load_dotenv

load_dotenv()  

class Settings:
    MODEL_PATH = os.getenv("MODEL_PATH")

settings = Settings()
