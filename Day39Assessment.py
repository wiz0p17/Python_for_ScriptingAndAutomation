##“API Inventory Exporter”
"""
It should:

fetch API data
extract:
id
name
username
email
city
export CSV report"""


import csv
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url,timeout=5)

    response.raise_for_status()

    users = response.json()

    with open("user.csv","w",newline="") as file:
        result = csv.writer(file)
        
        result.writerow(["Id","Name","Username","Email","City"])

        for user in users:
            result.writerow([user["id"],user["name"],user["username"],user["email"],user["address"]["city"]])

    print("Your CSV File is created.!!")

except requests.exceptions.RequestException as e:
    print("AN error occoured :",e)