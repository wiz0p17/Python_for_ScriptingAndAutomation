
#every second
"""
import schedule
import time

def say_hello():
    print("Hello Vivek")

schedule.every(5).seconds.do(say_hello)

while True:
    schedule.run_pending()
    time.sleep(1)"""

"""
Program Starts
      ↓
Task Registered
      ↓
Loop Starts
      ↓
Check Schedule
      ↓
Time Reached?
      ↓
Run Function
      ↓
Repeat Forever"""


#run every minute:
"""
import schedule
import time

def say_hello():
    print("Hello Vivek")

schedule.every().minute.do(say_hello)

while True:
    schedule.run_pending()
    time.sleep(1)"""


#Run Every Hour

#schedule.every().hour.do(say_hello)


#Run Every Day

#schedule.every().day.do(say_hello)


#Run at Specific Time
#Run every day at 8:00 AM

#schedule.every().day.at("08:00").do(say_hello)


#☁️ Cloud Example

#Imagine EC2 monitoring.

import schedule
import time

def check_ec2():
    print("Checking Ec2 Health")

def generateReport():
    print("Report Generated")


schedule.every(5).seconds.do(check_ec2)
schedule.every(2).seconds.do(generateReport)

while True:
    schedule.run_pending()
    time.sleep(1)



