#Daily Server Report Email

#Email should contain:
"""Subject: Daily Server Report

Server: EC2-Web

CPU: 72%

Memory: 60%

Status: Healthy"""

import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

sender = "hyperwiz0p@gmail.com"
reciever = "ivivekn005@gmail.com"

#password = os.environ.get("PASS")

message = """Subject: Ec2 Report

CPU Usage: 65%
Memory Usage: 55%

Server Healthy
"""

with smtplib.SMTP("smtp.gmail.com",587) as server:
    server.starttls()

    server.login(sender,os.environ.get("PASS"))

    server.sendmail(sender,reciever,message)

print("Mail Sent!...")





