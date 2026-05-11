#“GitHub User Fetcher”
"""
It should:

Fetch:

https://api.github.com/users/octocat
Print:
login
id
profile URL"""

import requests

try:
    response = requests.get("https://api.github.com/users/octocat",timeout=5)

    response.raise_for_status()

    data = response.json()

    print("Login: ",data["login"])
    print("Id: ",data["id"])
    print("Profile URL: ",data["html_url"])
    

except requests.exceptions.RequestException as e:
    print("Request failed ",e)
