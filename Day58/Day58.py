#EC2 Monitoring Simulator
"""
Every 10 seconds:

Check server health

Every 30 seconds:

Generate report

And save everything into log files."""

from pathlib import Path
import random
from datetime import datetime
import schedule
import time

Path("./Day58/logs").mkdir(exist_ok=True)

Path("./Day58/reports").mkdir(exist_ok=True)

#Create Monitoring Function
def monitor_server():
    
    cpu = random.randint(20,100)
    memory = random.randint(30,100)

    logCPU = (
        f"{datetime.now()}"
        f"CPU usage: {cpu}%"
    )

    logMemory = (
        f"{datetime.now()}"
        f"Memory usage: {memory}%\n"
    )

    print(logCPU)
    print(logMemory)

    filename = (f"log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log")
    with open(f"./Day58/logs/{filename}","a") as file:
        file.write(logCPU)
        file.write(logMemory)

#Create Report Function
def generate_report():

    report = (
        f"Report Generated: "
        f"{datetime.now()}"
    )

    print(report)

    filename = (f"report_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt")

    with open(f"./Day58/reports/{filename}","a") as file:
        file.write(report)

#Schedule Tasks

schedule.every(10).seconds.do(monitor_server)

schedule.every(30).seconds.do(generate_report)

while True:
    schedule.run_pending()
    time.sleep(1)