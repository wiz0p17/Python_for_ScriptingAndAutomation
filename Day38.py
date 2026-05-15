#📅 Day 38 – Authentication & Secure API Usage
"""
From your roadmap :

✅ Understand API authentication
✅ Use Bearer tokens
✅ Store secrets securely
✅ Build secure API clients"""


"""
🔑 2. Common Authentication Types
Type	        Example
API Key	        x-api-key: abc123
Bearer Token	Authorization: Bearer TOKEN
Basic Auth	    username/password
OAuth	        Google/GitHub login
"""

#📌 Send Request
"""
import requests

headers = {
    "x-api-key": "myapiKey"
}

response = requests.get("https://api.example.com/data",headers=headers)

print(response.status_code)"""

"""
import os 
from dotenv import load_dotenv

load_dotenv()

Token = os.getenv("TOKEN")

print(Token)

ApiToken = os.getenv("API_TOKEN")

print(ApiToken)"""


#🔥 7. Full Secure Request Example
"""
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("API_TOKEN")

header = {
    "Authorization" : f"Bearer {token}"
}

response = requests.get("https://api.github.com/user",headers= header,timeout=5)

print(response.status_code)

if response.status_code == 401:
    print("Unauthorized!!")"""


#🛡️ 9. Production Safety Pattern
"""
import os 
from dotenv import load_dotenv
import requests

load_dotenv()

token = os.getenv("API_TOKEN")

header = {
    "Authorization": f"bearer {token}"
}

try:
    response = requests.get("https://api.github.com/user",headers=header,timeout=5)

    print(response.status_code)

    response.raise_for_status()


except requests.exceptions.RequestException as e:
    print("API error :",e)"""



##🧪 10. Mini Practice (DO THIS)

#👉 Create .env

import os 
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("API_TOKEN")

print(token)