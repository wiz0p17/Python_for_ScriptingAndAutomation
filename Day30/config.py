import os 
from dotenv import load_dotenv

load_dotenv()

def apiKeyGetter(name):
    if name == "API_KEY":
        return os.getenv("API_KEY")
    
    elif name == "Environment":
        return os.getenv("Environment")

