#“Mini Cloud Analytics Dashboard”
"""
Your tool should:

fetch API data
create DataFrame
generate:
bar chart
line chart
save dashboard image"""

import pandas as pd
import matplotlib.pyplot as plt
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url,timeout=5)

data = response.json()

df = pd.DataFrame(data)

#line chart
plt.plot(df["username"],df["id"])

plt.xlabel("Username")
plt.ylabel("Ids")

#plt.savefig("data.png")

#bar chart
plt.figure(figsize=(14,5))
plt.bar(df["username"],df["id"])

plt.xlabel("Username")
plt.ylabel("Ids")
plt.grid(True)

plt.show()