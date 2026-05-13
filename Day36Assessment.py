#“API User Creator”
"""
It should:

Send:
name
role
Print:
created ID
returned data"""

import requests

url = "https://jsonplaceholder.typicode.com/users"

payload = {
    "name":"Vivek Negi",
    "role":"Xyz.com"
}

try:
    response = requests.post(url,json=payload,timeout=5)

    response.raise_for_status()

    data = response.json()

    print("Created ID: ",data["id"])
    print(data)

except requests.exceptions.RequestException as e:
    print("Request failed : ",e)