#Assignment
"""
Build:

EC2 Health Report Generator

Collect:

hostname
whoami
uptime
free -m
df -h

Save everything into:

ec2_report.txt"""


import subprocess
from datetime import datetime

commands = [
    "hostname",
    "whoami",
    "uptime",
    "df -h"
]

with open("sample.txt","w") as file:

    file.write(f"report: {datetime.now()}\n\n")

    for cmd in commands:
        result = subprocess.run(cmd,shell=True,capture_output=True,text=True)

        file.write(f"{cmd}:\n{result.stdout}\n")

print("File Created..!!")