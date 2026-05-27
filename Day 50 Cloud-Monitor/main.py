#📅 Day 50 – DevOps Monitoring Automation Project
"""
From your roadmap :

✅ Combine all concepts
✅ Build real automation workflow
✅ Create monitoring system
✅ Generate reports & dashboards"""


#🌐 5. Step 1 – Fetch API Data

#📁 9. Create Folders Automatically

from pathlib import Path

Path("reports").mkdir(exist_ok=True)
Path("Charts").mkdir(exist_ok=True)
Path("Logs").mkdir(exist_ok=True)
currnetPath = Path(".")

import requests 

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url,timeout=5)

user = response.json()

#📦 6. Convert JSON → DataFrame

import pandas as pd

df = pd.DataFrame(user)

#📄 7. Generate CSV Report

df.to_csv(f"{currnetPath}/reports/user_report.csv",index=False)

#📊 8. Create Dashboard Chart

import matplotlib.pyplot as plt

plt.bar(df["username"],df["id"])

plt.xlabel("Username")

plt.ylabel("IDs")

plt.savefig(f"{currnetPath}/Charts/DashDashboard.png")


#⏰ 10. Add Timestamped Files

from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
 

with open(f"{currnetPath}/Logs/monitor.logs","a") as file:
    file.write(f"{timestamp} Report generated\n")


print("Automation Completed")

#Full project code
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from datetime import datetime

# Create folders
Path("reports").mkdir(exist_ok=True)
Path("charts").mkdir(exist_ok=True)
Path("logs").mkdir(exist_ok=True)

# Timestamp
timestamp = datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S"
)

# Fetch API data
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

# Convert to DataFrame
df = pd.DataFrame(users)

# Save CSV report
csv_file = (
    f"reports/users_{timestamp}.csv"
)

df.to_csv(csv_file, index=False)

# Create chart
plt.figure(figsize=(10, 5))

plt.bar(
    df["username"],
    df["id"]
)

plt.title("User Dashboard")

chart_file = (
    f"charts/dashboard_{timestamp}.png"
)

plt.savefig(chart_file)

# Save logs
with open("logs/monitor.log", "a") as file:

    file.write(
        f"{datetime.now()} "
        f"Report Generated\n"
    )

print("Automation Completed!")"""