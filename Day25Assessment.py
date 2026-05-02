#“Process Pipeline Tool”
"""
It should:

Run:
ps aux
filter with grep
sort output
store result in log file"""


import logging
import subprocess

logging.basicConfig(filename="assessment.log",level=logging.INFO)

p1 = subprocess.Popen(["ps","aux"],stdout=subprocess.PIPE,text = True)

p2 = subprocess.Popen(["grep","python"],stdin = p1.stdout,stdout = subprocess.PIPE,text=True)

p3 = subprocess.Popen(["sort"],stdin = p2.stdout,stdout = subprocess.PIPE,text=True)

output = p3.communicate()[0]

logging.info(f"{output}\n")

