#for Day 23.py

from dotenv import load_dotenv
import os

load_dotenv()

"""load_dotenv(): This looks for a file named .env in your project folder. It reads the "key=value" pairs inside that file and adds them to your system's environment variables."""

if not os.getenv("API_KEY"):
    print("Missing API key")

class Config:
    APP_ENV = os.getenv("APP_ENV","dev")
    API_KEY = os.getenv("API_KEY")
    Timeout = int(os.getenv("TIMEOUT",10))

    @staticmethod
    def validate():
        if not Config.API_KEY:
            raise ValueError("API_KEY is required")
        
#---------------------------------------------------------------------------------------------