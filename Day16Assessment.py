###“System Health Checker”

'''
It should:

Run:
whoami
pwd
df -h
Print outputs clearly'''

import subprocess

commands = {
    "User" : ["whoami"],
    "Current Directory": ["pwd"],
    "Disk Space": ["df","-h"]
}

for name,cmd in commands.items():
    result = subprocess.run(cmd,capture_output=True,text=True)

    print(f"\nProcess Name --> {name}")
    print(result.stdout)