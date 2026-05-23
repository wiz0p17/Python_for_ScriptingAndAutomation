#📅 Day 46 – Automated Monitoring Dashboard
"""
From your roadmap :

✅ Fetch API data
✅ Process with pandas
✅ Visualize automatically
✅ Build monitoring workflow"""
"""
import requests

url ="https://jsonplaceholder.typicode.com/users"

response = requests.get(url,timeout=5)

users = response.json()"""

#print(users[0])

#Convert API Data to DataFrame

#Imagine JSON boxes 📦 becoming Excel sheet 📊
"""
import pandas as pd

df = pd.DataFrame(users)

#🔍 5. Extract Useful Data

names = df["name"]

print(names)"""

#Create Visualization
"""
import matplotlib.pyplot as plt

plt.bar(df["username"],df["id"])

plt.title("User IDs")

plt.xlabel("Names")
plt.ylabel("IDs")

plt.show()
"""


#🔥 8. Full Automation Workflow

import pandas as pd 
import requests 
import matplotlib.pyplot as plt


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url,timeout=5)

data = response.json()

df = pd.DataFrame(data) 

print(df.head())

## creating a bar chart of the response data

plt.figure(figsize=(14,5))

plt.bar(df["username"],df["id"])

plt.title("User name and ID bar chart")

plt.xlabel("usename")

plt.ylabel("IDs")

plt.show()

plt.savefig("UserData.png")

print("file created of User and Id")

