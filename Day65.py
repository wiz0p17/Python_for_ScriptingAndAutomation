"""Most people think:

Python Script
     ↓
Does One Task"""

#But advanced automation systems work like:

"""Python
  ↓
Creates Python
  ↓
Runs Python
  ↓
Schedules Python
  ↓
Monitors Python"""

#Example 1: Generate Python Scripts Automatically
"""
Imagine you manage 100 servers.

Instead of writing 100 scripts:

check_web_server.py
check_db_server.py
check_cache_server.py
...

You can generate them."""
import schedule
import time
import subprocess

def monitoring():
    servers = ["web","db","cache"]

    for server in servers:
        with open(f"{server}_monitor.py","a") as file:
            file.write(f'\nprint(2+2)')


    for server in servers:
        result = subprocess.run(["python3", f"{server}_monitor.py"],capture_output=True,text=True)
        print(f"Showing content of file: {server}_monitor.py")
        print(result.stdout)

schedule.every(10).seconds.do(monitoring)

while True:
    schedule.run_pending()
    time.sleep(1)
