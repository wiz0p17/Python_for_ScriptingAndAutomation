#“Secure API Client”
"""
It should:

Load token from .env
Add Bearer token header
Make API request safely
Handle errors properly"""


import requests
import os 
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("API_KEY")

header = {
    "Authorization" : f"Bearer {token}"
}

try: 
    response = requests.get("https://api.github.com/users",headers=header,timeout=5)

    print(response.status_code)

    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print("API Error :",e)



