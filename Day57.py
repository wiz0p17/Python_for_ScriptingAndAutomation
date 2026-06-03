#What is an Idempotent Script?
"""
Big word 😄

Let's make it simple.

An idempotent script is: A script that can run multiple times
without causing problems."""

"""Why Cloud Engineers Love Idempotency

Imagine:

Cron Job
Runs every hour

If the script crashes because something already exists:

❌ Monitoring stops

❌ Backups fail

❌ Reports fail"""


from pathlib import Path

Path("reports").mkdir(exist_ok=True)

#Example 2 – File Creation

#Bad:

with open("sample.txt","x") as file:
    file.write("AWS")

#better:

from pathlib import Path

file = Path("sample.txt")

if not file.exists():
    file.write_text("AWS")


#Example 3 – Installing Packages
"""
Bad:

pip install requests

every time.

Better:"""


try:
    import requests

except ImportError:
    print ("Install Requests")


#Example 4 – Logging
#bad:

with open("sample.txt") as file:
    file.write("started")

#better:

with open("sample.txt") as file:
    file.write("Started\n")


#Cloud Example – EC2 Monitor
#bad:

with open("dailyreport.csv","w") as file:
    file.write("...")


#better:

from datetime import datetime

filename = (
    f"report{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt"
)


#🛡️ Defensive Programming
"""
Before doing anything:

Ask:

Does it already exist?

Examples:

if file.exists():
if folder.exists():
if server_running:"""


#Real DevOps Pattern
"""
Instead of:

start_server()

Do:

if not server_running():
    start_server()"""


#Practice

from pathlib import Path

folder = Path("reports")

folder.mkdir(exist_ok=True)

print("log folder is ready!!!")





