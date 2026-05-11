#🌐 3. First HTTP GET Request
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)

#🔥 5. Parse JSON Response
import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data)


#📌 6. Access API Data

print(data["current_user_url"])

#⚠️ 7. Check Status Codes (VERY IMPORTANT)
if response.status_code == 200:
    print("Success")
else:
    print("Failed")

#👉 Fetch fake users:

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print(user["name"])


#🔥 9. Add Error Handling

import requests

try:
    response = requests.get("https://api.github.com")

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

#⏳ 10. Add Timeout (VERY IMPORTANT)
requests.get(url, timeout=5)


"""🧪 11. Mini Practice (DO THIS)

👉 Fetch GitHub API:"""

import requests

response = requests.get("https://api.github.com")

print(response.status_code)