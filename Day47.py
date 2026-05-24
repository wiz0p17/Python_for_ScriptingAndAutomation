#📅 Day 47 – File Automation & Report Management
"""
From your roadmap :

✅ Automate file generation
✅ Organize reports
✅ Use timestamps
✅ Build structured automation outputs"""

#“Automated Monitoring Report System”
"""
Your tool will:
✅ create reports
✅ generate timestamped filenames
✅ organize folders automatically"""

from pathlib import Path
from datetime import datetime
import pandas as pd

reports_dir = Path("Reports")

reports_dir.mkdir(exist_ok=True)

print("folder Ready!")

#generate timestamp 

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

print(timestamp)

#create dynamic file name

filename = f"report_{timestamp}.txt"

print(filename)

#save report file

report_path = reports_dir / filename

with open(report_path, "w") as file:
    file.write("System Report \n")
    file.write("CPU Usage 70%\n")

print("Report Saved")

#data 
data = {
    "Instances" : ["Ec2-1","Ec2-2"],
    "CPU" : [70,90]
}

df = pd.DataFrame(data)

#dynamic file path 

file_path = reports_dir / f"report_{timestamp}.csv"

df.to_csv(file_path,index=False)

print(f"File Saved {file_path}")
