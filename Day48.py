"""📅 Day 48 – Periodic Automation & Scheduling Concepts

From your roadmap :

✅ Run scripts repeatedly
✅ Understand scheduling
✅ Build monitoring loops
✅ Learn automation cycles"""

#“Mini Monitoring Loop”


#💤 4. Add Delay with time.sleep()

"""import time

while True:
    print("Hello")

    time.sleep(3)"""


#🔥 5. Monitoring Loop Example

#📦 6. Add Timestamp
"""
from datetime import datetime
import time

count = 0

while(count<5):
    print("Collecting Monitoring Data...")
    print(datetime.now())
    time.sleep(3)
    count+=1    
"""



#🔥 7. Full Monitoring Cycle
"""
import time
from datetime import datetime

for i in range(5):
    print(f"[{datetime.now()}] checking CPU...")

    time.sleep(5)
"""

#📄 8. Save Logs Automatically
"""
with open("file.log","a") as file:
    file.write(f"[{datetime.now()}] Checking CPU...")"""


#🔥 9. Full Automation Script

import time
from datetime import datetime

for i in range(5):
    log = f"{datetime.now()} Checking CPU Utilization\n"

    print(log)

    with open("file.log","a") as file:
        file.write(log)

    time.sleep(2)

print("Monitoring Finished!")