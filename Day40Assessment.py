##“Multi User Fetcher”
"""
It should:

take user ID
fetch API
print:
name
email
city
company
export CSV report"""


import requests
import csv
import argparse

parser = argparse.ArgumentParser("Multi User Fetcher")

parser.add_argument("--user",required=True)

args = parser.parse_args()

url = f"https://jsonplaceholder.typicode.com/users/{args.user}"

try:
    response = requests.get(url,timeout=5)

    response.raise_for_status()

    user = response.json()

    print("\nUser Details")

    print("Name: ",user["name"])
    print("Email: ",user["email"])
    print("User: ",user["address"]["city"])
    print("Company: ",user["company"]["name"])

    with open("file.csv","a",newline="") as file:
        input = csv.writer(file)
       
        input.writerow(["Name","Email","City","Company Name"])

        input.writerow([user["name"],user["email"],user["address"]["city"],user["company"]["name"]])

    print("Data written in CSV")

except requests.exceptions.RequestException as e:
    print("An error occoured : ",e)