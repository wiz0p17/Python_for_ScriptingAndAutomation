#Assignment
"""
Build:EC2 Alert System

Requirements:

Generate random CPU values
random.randint(20, 100)
If CPU > 85

Send Slack alert:⚠️ CPU Threshold Exceeded
                    Run every 15 seconds using Schedule Library."""


import requests
import time
import random
import schedule

def sendSlackAlert(text):
    
    url = "https://webhook.site/77f02b96-4b6f-412c-a8d5-90b3576088fc"

    requests.post(url,json={"text":text})

    print("Message sent to slack")


def monitor():
    cpu = random.randint(20,100)

    print(f"CPU Utilization: {cpu}%")

    if cpu > 85:
        sendSlackAlert(f"CPU Utilization: {cpu}")
    

schedule.every(30).seconds.do(monitor)

while True:
    schedule.run_pending()
    time.sleep(1)

    