#“Mini EC2 Monitor”
"""
Your script should:
✅ run every 2 sec
✅ generate fake CPU values
✅ save logs automatically
✅ include timestamps"""

import random
import time
from datetime import datetime

for i in range(5):

    cpu = random.randint(20, 90)
    log = f"{datetime.now()} CPU Utilizatioion = {cpu}\n"

    print(log)

    with open("file.log","a") as file:
        if cpu > 60:
            file.write(log)

    time.sleep(3)

print("File created and written in file.log")