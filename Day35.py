#📅 Day 35 – Query Params, Headers & Auth Basics
"""
From your roadmap :

✅ Send query parameters
✅ Use request headers
✅ Understand API authentication basics"""

"""
import requests

params = {
    "page":2
}

params2 = {
    "userId": 1
}

response = requests.get("https://jsonplaceholder.typicode.com/posts",params=params)

print(response.url)
print(response.json())"""


#🔥 3. Multiple Query Parameters

"""import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts",params={"userID":1},timeout=5)

posts = response.json()

for post in posts:
    print(post["title"])"""


"""📡 4. Headers (headers=)

Headers provide metadata to API.

Examples:

authentication
content type
client info
"""
"""
import requests

headers = {"User-Agent": "Python Script"}

response = requests.get("https://api.github.com",headers=headers)

print(response.json())"""


##🔐 5. API Authentication Basics

#Authorization: Bearer TOKEN
"""
headers = {
    "Authorization": "Bearer mytoken"
}"""


"""⚠️ 6. NEVER Hardcode Tokens

❌ Bad:

TOKEN = "123456"

✅ Better:

import os

TOKEN = os.getenv("API_TOKEN")

👉 Use .env"""

#🔥 7. Real GitHub API Example
"""
import requests

headers = {
    "User-Agent": "Python-App"
}

response = requests.get("https://api.github.com/users/octocat",headers=headers,timeout=5)

data = response.json()

print(data["login"])"""


#🧪 8. Mini Practice (DO THIS)

"""👉 Fetch posts for user 1:"""

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts",params={"userId":1})

data = response.json()

print(data[0])