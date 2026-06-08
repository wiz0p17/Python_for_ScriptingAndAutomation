#System Information Collector
"""
Collect: pwd
        whoami
        uptime
        df -h


Store results into: sample.txt"""

import subprocess

commands = [["pwd"],["whoami"],["uptime"],["df","-h"]]

with open("sample.txt","a") as file:

    for command in commands:

        result = subprocess.run(command,capture_output=True,text=True)

        print(result.stdout)

        file.write(f"{command} : {result.stdout}\n")

print("file created")


