##📅 Day 40 – API + CLI Automation Tool
"""
From your roadmap :

✅ Combine APIs with CLI tools
✅ Accept user input
✅ Generate reports dynamically"""


#⚙️ 3. Step 1 – Setup CLI
"""
import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument("--user",required=True)

args = parser.parse_args()

print(args.user)"""

#🌐 4. Fetch API Data
"""
url = f"https://jsonplaceholder.typicode.com/users/{args.user}"

response = requests.get(url,timeout=5)

user = response.json()

print(user)"""

#🔍 6. Extract Useful Data
"""
print("-"*65)
print("User name: ",user["name"])
print("Email: ",user["email"])
print("City: ",user["address"]["city"])"""


#🔥 7. Full CLI API Tool
import csv
import argparse
import requests

parser = argparse.ArgumentParser(description="User fetch tool")

parser.add_argument("--user",required=True,help="User input")

args = parser.parse_args()

url = f"https://jsonplaceholder.typicode.com/users/{args.user}"

try:
    response = requests.get(url,timeout=5)

    response.raise_for_status()

    user = response.json()

    print("\n User Information")
    print("-"*50)
    print("Name: ",user["name"])
    print("Email: ",user["email"])
    print("City: ",user["address"]["city"])

    with open("user.csv","w",newline="") as file:
        input = csv.writer(file)

        input.writerow(["Name","Email","City","Company Name"])

        input.writerow([user["name"],user["email"],user["address"]["city"],user["company"]["name"]])

except requests.exceptions.RequestException as e:
    print("An error occoured: ",e)
