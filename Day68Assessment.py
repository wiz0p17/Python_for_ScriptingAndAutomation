#Smart Log Analyzer
"""
Requirements:

Read:

server.log

Extract:

All ERROR messages

All WARNING messages

Generate:

report.txt

Example:

ERRORS FOUND: 2

ERROR Database Failed

ERROR S3 Upload Failed

WARNINGS FOUND: 1

WARNING High CPU"""


import re

output = ""

with open("logs.log","r") as file:
    text = file.read()

warning = re.findall(r"WARNING.*",text)

output += f"Warning Found: {len(warning)}"

for war in warning:
    output += f"\n{war}"

output += f"\n"

response = re.findall(r"ERROR.*",text)

output += f"\nError Found: {len(response)}"

for res in response:
    output += f"\n{res}"

with open("report.txt","w") as file:
    file.write(output)

print("report created...")


