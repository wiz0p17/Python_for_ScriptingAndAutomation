#“System Report CSV Exporter”
"""
It should:

Store:
username
OS
skill
Export to CSV file"""

import csv
import os

data = [
    ["username","OS","Skill"],
    [os.getenv("USER"),os.name,"Python Automation"]
]

with open("Report.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerows(data)

print("CSV Report Created!!!")

with open("Report.csv","r") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row[0],row[1],row[2])