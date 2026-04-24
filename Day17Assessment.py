##“Robust System Checker”
'''
It should:

Run:
whoami
uptime
one wrong command
Handle success + failure properly
Print clean output'''

import subprocess

command = [["whoami"],["uptime"],["ls","hell"]]

for cmd in command:
    try:
        result = subprocess.run(cmd,capture_output=True,text=True,check=True)

        print(f"\nCommand✅ : {" ".join(cmd)}")
        print(result.stdout)
    
    except subprocess.CalledProcessError as e:
        print(f"\nError in file❌ : {" ".join(cmd)}")
        print(e.stderr)



