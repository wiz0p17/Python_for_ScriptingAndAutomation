#“Command Runner with Timeout”

"""
It should: Accept:  command
                    timeout
                    Run command
                    Stop if timeout exceeded"""

import subprocess

cmd = ["sleep","5"]
timeout = 2

try:
    process = subprocess.run(cmd,timeout)

    print("command finished")

except subprocess.TimeoutExpired:
    print("Command Time out!!!")