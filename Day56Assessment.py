#Mini Cloud Assignment

"""Create:

def monitor_server():
    print("Server Healthy")

Run: Every 15 seconds

Expected Output:    Server Healthy
                    Server Healthy
                    Server Healthy"""

import schedule
import time

def monitor_server():
    print("Server Healthy")

schedule.every(15).seconds.do(monitor_server)

while True:
    schedule.run_pending()
    time.sleep(1)
