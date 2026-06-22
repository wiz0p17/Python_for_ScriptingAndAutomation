print("Day 69 Assessment Code")


print("Today is my birthday!!!!")




#System Alert Manager

"""
Generate:

cpu
memory
disk

using:

random.randint()

Rules:

CPU > 85
Memory > 80
Disk > 90

Trigger alerts.

Example:

ALERT: CPU 92%

ALERT: Memory 88%"""


def notify(message):
    print(message)


import random

cpu = random.randint(20,100)
disk = random.randint(20,100)
memory = random.randint(20,100)

if cpu > 85:
    notify(f"ALERT: CPU = {cpu}%")

if memory > 80:
    notify(f"ALERT: Memory = {memory}%")

if  disk > 90:
    notify(f"ALERT: Disk= {disk}%")


