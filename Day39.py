##📅 Day 39 – API → JSON → CSV Automation
"""
From your roadmap :

✅ Fetch API data
✅ Process JSON
✅ Export reports to CSV
✅ Build real automation workflow"""


#👉 “GitHub User Report Generator”
"""
Your tool will:

fetch users from API
parse JSON
save report into CSV"""


#Step 1 – Fetch API Data

import requests
"""
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url,timeout=5)

users = response.json()

print(users[0])

for user in users:
    print("name: ",user["name"])
    print("email: ",user["email"])
    print("-"*80)
"""

#Export to CSV
"""
import csv

with open("user.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name","Email"])

    for user in users:
        writer.writerow([user["name"],user["email"]])

print("CSV file Created.!")"""


#🔥 7. Full Automation Script

import csv
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url,timeout=5)

    response.raise_for_status()

    users = response.json()

    with open("user.csv","w",newline="") as file:
        output = csv.writer(file) 

        output.writerow(["Id","Name","Email"])    

        for user in users:
            output.writerow([user["id"],user["name"],user["email"]])

    print("File Created Successfully..!!")

except requests.exceptions.RequestException as e:
    print("An error occoured :",e)