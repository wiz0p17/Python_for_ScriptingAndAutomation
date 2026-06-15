#Monitoring Config Reader
"""
Config:

{
    "cpu_threshold": 80,
    "memory_threshold": 75,
    "disk_threshold": 85
}

Python should print:

CPU Threshold: 80

Memory Threshold: 75

Disk Threshold: 85"""

import json

with open("config.json","r") as file:
    config = json.load(file)

    vars = ["cpu_threshold","memory_threshold","disk_threshold"]
    for var in vars:
        print(f"{var} : {config[var]}")