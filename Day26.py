#📅 Day 26 – Advanced Workflows (CLI + Subprocess + Logging + Error Handling)

"""From your roadmap :

✅ Combine all concepts
✅ Build robust automation tools
✅ Handle errors + logs + CLI together"""



#Features of Today’s Tool
"""
Your script will:

    ✔ Accept CLI input
    ✔ Run system commands
    ✔ Log output
    ✔ Handle errors
    ✔ Support verbose mode"""

import subprocess
import logging
import argparse


logging.basicConfig(filename="Day26Logs.log",level=logging.INFO,format = "%(asctime)s - %(levelname)s - %(message)s")

parser = argparse.ArgumentParser(description="System Monitor Tool")

parser.add_argument("--check",choices=["disk","cpu","user"],help="Type of System Check",required=True)

parser.add_argument("--verbose",action="store_true",help="Detailed Output")

args = parser.parse_args()

def run_command(cmd):
    try:
        result = subprocess.run(cmd,capture_output=True,text=True,check=True)

        logging.info(f"Command Executed : {" ".join(cmd)}")

        return result.stdout
    
    except subprocess.CalledProcessError as e:
        logging.error(f"Error Occoured :{e.stderr}")

        return "Command failed!!!"
    
if args.check == "disk":
    output = run_command(["df","-h"])

elif args.check == "cpu":
    output = run_command(["uptime"])

elif args.check == "user":
    output = run_command(["whoami"])


if args.verbose:
    print("Detailed Output :",output)

else:
    print(output)

logging.info("Script Completed!")