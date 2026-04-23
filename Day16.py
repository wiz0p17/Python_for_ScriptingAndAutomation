##Running Shell Commands with Python (subprocess)

'''✅ Run shell commands from Python
✅ Replace basic Bash scripts
✅ Start automating system-level tasks'''

##Basic Command Execution

import subprocess

"""subprocess.run(["ls"])"""

'''result = subprocess.run(["ls","-l"],capture_output=True,text=True)

print(result.stdout)
print(result.stderr)
print(result.returncode)'''


'''subprocess.run(["whoami"])
subprocess.run(["pwd"])
subprocess.run(["date"])'''


'''import subprocess

result = subprocess.run(["df","-h"],capture_output=True,text=True)

print(result.stdout)'''

import subprocess

commands = ["pwd","whoami","uptime"]

for cmd in commands:
    result = subprocess.run([cmd],capture_output=True,text=True)
    
    print(f"-----{cmd}-----")
    print(result.stdout)



"""
⚠️ 8. Important Notes
❌ Avoid this:
subprocess.run("ls -l", shell=True)

👉 Unsafe (security risk)

✅ Use this:
subprocess.run(["ls", "-l"])

👉 Safe & recommended"""