##📅 Day 22 – Mini Project (CLI + Subprocess + Env)

'''👉 “System Health CLI Tool”'''

"""This tool will:

Take input from CLI
Run system commands
Use environment variables
Display formatted output"""


'''Your script will:

✔ Accept:

--check disk | cpu | user

✔ Use:

subprocess → run commands
argparse → CLI
.env → config

✔ Output:

Clean system info'''

'''
import subprocess
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(description="System Health CLI tool")

parser.add_argument("--check",required=True,choices=["disk","cpu","user"],help="Pass parameter to check")

args = parser.parse_args()

env_var = os.environ.get("DB_URL")

print(f"Running in {env_var} environment\n")

try:
    if args.check == "disk":
        result = subprocess.run(["df","-h"],capture_output=True,text=True,check=True)
        print("Disk Usage \n",result.stdout)

    elif args.check == "cpu":
        result = subprocess.run(["uptime"],capture_output=True,text=True,check=True)
        print("CPU load \n",result.stdout)

    elif args.check == "user":
        result = subprocess.run(["whoami"],capture_output=True,text=True,check=True)
        print("Current User \n",result.stdout)

except subprocess.CalledProcessError as e:
    print("Commad Failed!!!")
    print(e.stderr)'''





#Your Assignment (🔥 Important)
'''
👉 Upgrade this tool:

Add:

--verbose flag
Logging (app.log)
--dry-run option'''




import subprocess
import os
import argparse
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(filename="CLItool.log",level=logging.INFO)

parser = argparse.ArgumentParser(description="System Health CLI tool")

parser.add_argument("--check",required=True,choices=["disk","cpu","user"],help="Pass parameter to check")
parser.add_argument("--verbose",help="to log the output in a file",action="store_true")
parser.add_argument("--dryrun",help="to only get output on screen not in log file",action="store_true")

args = parser.parse_args()

env_var = os.environ.get("DB_URL")

try:
    if args.dryrun:
        print(f"Running in {env_var} environment\n")
        if args.check == "disk":
            result = subprocess.run(["df","-h"],capture_output=True,text=True,check=True)
            print("Disk Usage \n",result.stdout)

        elif args.check == "cpu":
            result = subprocess.run(["uptime"],capture_output=True,text=True,check=True)
            print("CPU load \n",result.stdout)

        elif args.check == "user":
            result = subprocess.run(["whoami"],capture_output=True,text=True,check=True)
            print("Current User \n",result.stdout)
    
    elif args.verbose:
        logging.info(f"Running in {env_var} environment\n")
        if args.check == "disk":
            result = subprocess.run(["df","-h"],capture_output=True,text=True,check=True)
            logging.info(f"Disk Utilization \n{result.stdout}")

        elif args.check == "cpu":
            result = subprocess.run(["uptime"],capture_output=True,text=True,check=True)
            logging.info(f"CPU Load \n{result.stdout}")

        elif args.check == "user":
            result = subprocess.run(["whoami"],capture_output=True,text=True,check=True)
            logging.info(f"Current User \n{result.stdout}")

except subprocess.CalledProcessError as e:
    print("Commad Failed!!!")
    if args.verbose:
        logging.error(f"Error occoured \n{e.stderr}")

    elif args.dryrun:
        print(e.stderr)