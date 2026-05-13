#📅 Day 36 – POST Requests with requests
"""
From your roadmap :

✅ Send data to APIs
✅ Use POST requests
✅ Send JSON payloads"""
"""
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "Python Automation",
    "body" : "Learning APIs",
    "userId" : 1
}

response = requests.post(url, json= data)

print(response.status_code)
print(response.json())"""


#🔥 3. Why json= is Important
"""
✅ Correct:

requests.post(url, json=data)

❌ Avoid:

requests.post(url, data=data)

👉 json= automatically:

converts dictionary → JSON
adds correct content-type header"""

#📦 4. Sending Headers with POST
"""
headers = {
    "Authorization": "Bearer TOKEN"
}

📌 Example

response = requests.post(
    url,
    json=data,
    headers=headers
)"""


#⚠️ 5. Error Handling (VERY IMPORTANT)
"""
import requests

try:
    data = {
        "title": "Python automation",
        "body" : "Python",
        "userId" : 1
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts",json = data)

    response.raise_for_status()
    print(response.json())

except requests.exceptions.RequestException as e:
    print("Request failed",e)
"""

#⏳ 6. Add Timeout
"""
requests.post(url, json=data, timeout=5)

👉 Production safety 🔥"""


#🌍 7. Real API Example
"""
import requests

try :
    
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "AWS Cloud automation",
        "body": "learning AWS cloud automation with Python.",
        "userId": 1
    }

    response = requests.post(url,json=payload,timeout=5)

    response.raise_for_status()

    data = response.json()
    print("ID: ",data["id"])

except requests.exceptions.RequestException as e:
    print("Request failed :",e)

"""


##🧪 8. Mini Practice (DO THIS)

#👉 Send fake user data:

import requests 

payload = {
    "name":"vivek",
    "role":"Cloud Engineer"
}

response = requests.post("https://jsonplaceholder.typicode.com/users",json = payload,timeout=5)

print(response.json())