"""📅 Day 34 – HTTP Requests with requests

From your roadmap :

✅ Use APIs
✅ Fetch live data
✅ Send HTTP requests
✅ Handle API responses"""

"""
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)
"""

#🔥 5. Parse JSON Response
"""
import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data)"""

#📌 6. Access API Data

"""print(data["current_user_url"])"""

#⚠️ 7. Check Status Codes (VERY IMPORTANT)
"""
if response.status_code == 200:
    print("Success")
else:
    print("failed")"""


#🌍 8. Real API Example
"""
👉 Fetch fake users:"""

"""import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print(user["name"])"""


#🔥 9. Add Error Handling
"""
import requests

try:
    response = requests.get("https://api.github.com")

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.RequestException as e:
    print("Request Failed",e)"""


#⏳ 10. Add Timeout (VERY IMPORTANT)
"""
import requests

try:
    response = requests.get("https://api.github.com",timeout=5)

    response.raise_for_status()

    data = response.json()
    
    print(data)

except requests.exceptions.RequestException as e:
    print("Request Failed ",e)"""


#🧪 11. Mini Practice (DO THIS)
"""
👉 Fetch GitHub API:"""

import requests

response = requests.get("https://api.github.com",timeout=5)

print(response.status_code)
