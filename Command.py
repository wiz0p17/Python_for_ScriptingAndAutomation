import subprocess

def run_command(cmd):
    result = subprocess.run(cmd,capture_output=True,check=True,text=True)
    return result.stdout

def check_disk():
    return run_command(["df","-h"])

def check_cpu():
    return run_command(["uptime"])

def check_user():
    return run_command(["whoami"])


