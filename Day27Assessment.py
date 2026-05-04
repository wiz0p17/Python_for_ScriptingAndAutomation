#“Reliable Monitor Tool”
"""
It should:

Run command
Retry 3 times if fails
Log success/failure"""


import subprocess
import time
import logging


logging.basicConfig(filename="Reliable.log",level=logging.INFO)

def command_runner(cmd,retry = 3):
    for attempt in range(retry):
        try:
            result = subprocess.run(cmd,capture_output=True,check=True,text=True)

            return result.stdout
        
        except Exception as e:
            print(f"Attempt {attempt+1} failed...")
            time.sleep(2)

output = command_runner(["df","-h"])

print(output)
