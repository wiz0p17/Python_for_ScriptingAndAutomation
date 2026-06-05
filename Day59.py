#Email Automation with smtplib

#What is SMTP?

"""SMTP = Simple Mail Transfer Protocol

Think:

Python Script
      ↓
SMTP Server
      ↓
Recipient Inbox

SMTP is basically the post office for emails."""
import os
from dotenv import load_dotenv
import smtplib
import time

load_dotenv()

sender = "hyperwiz0p@gmail.com"
receiver = "abhijeetsinghadv02@gmail.com"
password = os.environ.get("PASS")

message = """Subject: Test Email

Hello from VIVEK!
"""
while True:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()

        server.login(sender,password)

        server.sendmail(sender,receiver,message)
    
    time.sleep(2)

print("Email Sent!!..")

