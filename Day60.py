#🎯 Slack Notifications

#Instead of checking logs or email, your script can instantly send alerts to a Slack channel.

#Step 3: First Slack Message

import requests


def sendSlackAlert(text):
    webhook_url = "https://webhook.site/77f02b96-4b6f-412c-a8d5-90b3576088fc"

    requests.post(webhook_url,json={"text":text})

print("message sent")



#Combine With Schedule Library

import schedule
import time
import random

def monitor():
    cpu = random.randint(20,100)

    print(f"cpu utilization: {cpu}%")

    if cpu > 90:
        sendSlackAlert(f"🚨 CPU Alert: {cpu}%")

schedule.every(10).seconds.do(monitor)

while True:
    schedule.run_pending()
    time.sleep(1)




