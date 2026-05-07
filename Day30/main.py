from commands import runCommand
from config import apiKeyGetter
from utils import retry_logic
import logging
import argparse

logging.basicConfig(filename="day30Code.log",level=logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument("--check",choices=["disk","cpu","user"],required=True,help="Enter what you want to check")

parser.add_argument("--verbose",action="store_true",help="if you want to forcefully execute command")

args = parser.parse_args()

print("Hello from",apiKeyGetter("Environment")," By api key",apiKeyGetter("API_KEY"))


if args.verbose:
    if args.check == "disk":
        output = retry_logic(["df","-h"])
        print("Output = \n",output)
        logging.info(f"Output From verbose = \n{output}")

    elif args.check == "cpu":
        output = retry_logic(["uptime"])
        print("Output = \n",output)
        logging.info(f"Output From verbose = \n{output}")

    elif args.check == "user":
        output = retry_logic(["whoami"])
        print("Output = \n",output)
        logging.info(f"Output From verbose = \n{output}")

else:
    if args.check == "disk":
        output = runCommand(["df","-h"])
        print("Output = \n",output)
        logging.info(f"Output = \n{output}")

    elif args.check == "cpu":
        output = runCommand(["uptime"])
        print("Output = \n",output)
        logging.info(f"Output = \n{output}")

    elif args.check == "user":
        output = runCommand(["whoami"])
        print("Output = \n",output)
        logging.info(f"Output = \n{output}")





