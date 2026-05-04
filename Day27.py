#📅 Day 27 – Advanced Error Handling & Retry Logic
"""
From your roadmap :

✅ Advanced try/except patterns
✅ Retry logic
✅ Build fault-tolerant scripts"""


#⚠️ Basic try/except (Recap)
"""
try:
    result = subprocess.run(["ls","-l"],check = True)

except subprocess.CallProcessError:
    print("Command Failed")"""


##🔥 Retry Logic (VERY IMPORTANT)
"""
import subprocess
import time

for attempt in range(3):
    try:
        result = subprocess.run(["ls","wrong_folder"],check= True)

        print("Success")
        break
    except subprocess.CalledProcessError:
        print(f"Attempt {attempt+1} failed")
        time.sleep(2)"""


##Clean Retry Function (BEST PRACTICE)


"""import time
import subprocess

def run_with_retry(cmd,retries = 3):
    for attempt in range(retries):
        try:
            result = subprocess.run(cmd,capture_output=True,text = True,check=True)

            return result.stdout

        except subprocess.CalledProcessError:
            print(f"Attempt {attempt+1} failed")
            time.sleep(3)


output = run_with_retry(["ping","-c","2","google.com"])

print(output)"""

"""
import subprocess

try:
    subprocess.run(["ls","abc"],check=True)

except FileNotFoundError:
    print("Command Not found!!!")

except subprocess.CalledProcessError:
    print("Command Execution Failed!!!")

except Exception as E:
    print("Unexpected Error :",E)"""



#👉 Reliable Command Runner


import subprocess
import time

def command_runner(cmd,retries = 3):
    for attempt in range(retries):
        try:
            result = subprocess.run(cmd,capture_output=True,text=True,check=True)

            return result.stdout
        
        except Exception:
            print(f"Retrying {attempt+1} ...")
            time.sleep(2)

print(command_runner(["uptime"]))