#🚀 Day 62 – Advanced subprocess for DevOps Automation
"""
Yesterday you learned:

✅ subprocess.run()

✅ Capture command output

✅ Run Linux commands from Python"""

"""
import subprocess

process = subprocess.Popen(
    ["sleep", "10"],text=True
)

print("Program continues...")

result,error = process.communicate()

print(result)"""

"""import subprocess

process = subprocess.Popen(["date"],stdout=subprocess.PIPE,text=True)

output,error = process.communicate()

print(output)"""

"""
import subprocess

result = subprocess.run(["ls","Day30"],capture_output=True,text=True)

print("STDOUT:")
print(result.stdout)

print("STDERR:")
print(result.stderr)"""


#4️⃣ shell=True

#Sometimes Linux commands use shell features.

"""import subprocess

result = subprocess.run("ls | grep Day59",shell=True,capture_output=True,text=True)

print(result.stdout)"""


#RUN multiple commands.
"""
import subprocess

commands = [
    "pwd",
    "whoami",
    "date"
]

for cmd in commands:
    result = subprocess.run(cmd,text=True,capture_output=True)

    print(result.stdout)"""


#Linux health Checker

import subprocess
from datetime import datetime

commands = [
    "whoami",
    "uptime",
    "df -h"
]

with open("sample.txt","w") as file:

    file.write(f"report: {datetime.now()}\n\n")

    for cmd in commands:
        result = subprocess.run(cmd,shell=True,capture_output=True,text=True)

        file.write(f"{cmd}:\n{result.stdout}\n")

print("File Created..!!")

