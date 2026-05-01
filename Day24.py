#📅 Day 24 – Process Management (Popen, Timeouts, Control)

"""
✅ Manage running processes
✅ Handle timeouts
✅ Control execution flow
✅ Build monitoring scripts"""

'''
import subprocess

process = subprocess.Popen(["ls","-l"],stdout=subprocess.PIPE,text=True)

output = process.communicate()[0]

print(output)'''


"""import subprocess

try:
    result = subprocess.run(["sleep","5"],timeout=10,text=True,capture_output=True)
    print(result.stdout)


except subprocess.TimeoutExpired:
    print("Process took too long!!!")"""

'''
import subprocess
import time

process = subprocess.Popen(["sleep","10"])

time.sleep(2)

process.terminate()

if process.poll() is None:
    print("Still running")
else:
    print("Finished")

print("Process Terminated!!!")'''


#🔁 7. Real-Time Output (Advanced 🔥)

'''import subprocess


process = subprocess.Popen(["ping","-c","4","google.com"],stdout=subprocess.PIPE,text=True)

for line in process.stdout:
    print("live:",line)'''



#🔥 8. Real Automation Script

#👉 Process Monitor with Timeout

"""import subprocess


try:
    process = subprocess.run(["ping","-c","4","google.com"],capture_output=True,text=True,timeout=4)

    print(process.stdout)

except subprocess.TimeoutExpired:
    print("Ping took too long, stopping.....")
"""



"""
🧪 9. Mini Practice (DO THIS)

👉 Run a long command and stop it:"""


import time
import subprocess

process = subprocess.Popen(["top"])

time.sleep(3)

process.kill()

print(process.stdout)