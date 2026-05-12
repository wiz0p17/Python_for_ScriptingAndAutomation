#“GitHub Repo Fetcher”
"""
It should:

Fetch:

https://api.github.com/users/octocat/repos
Print:
repo name
repo URL"""

import requests

response = requests.get("https://api.github.com/users/octocat/repos",timeout=5)

files = response.json()

for data in files:
    print("Repo Name: ",data["name"])
    print("Repo URL: ",data["html_url"])
    print("-"*100)