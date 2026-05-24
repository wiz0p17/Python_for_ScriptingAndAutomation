#“Daily Cloud Report Generator”
"""
Your tool should:
✅ create reports/ folder
✅ generate timestamped CSV
✅ save monitoring report
✅ save chart image"""

from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

report_dir = Path("reports")

report_dir.mkdir(exist_ok=True)

print("Folder Created!")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(timestamp)
#data
data = {
    "Instances" : ["Ec2-1","Ec2-2"],
    "CPU" : [70,90]
}

df = pd.DataFrame(data)

#dynamic file structure for file

file_path = report_dir / f"report_{timestamp}.csv"

df.to_csv(file_path,index=False)

print("File created and save to ",file_path)

#dynamic file structure for chart
file_path_img = report_dir / f"dashboard_{timestamp}.png"

plt.bar(df["Instances"],df["CPU"],color = "orange")

plt.title("Ec2 CPU dashboard")

plt.xlabel("Instance")

plt.ylabel("CPU")

plt.grid(True)

plt.savefig(file_path_img)

print("Image created and saved to ",file_path_img)