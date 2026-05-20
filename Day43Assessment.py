#“EC2 Usage Analyzer”
"""
Create DataFrame:

Instance	Team	CPU
EC2-1	    DevOps	70
EC2-2	    Backend	50
EC2-3	    DevOps	90

Your tool should:

group by Team
calculate:
average CPU
max CPU
export CSV report"""


import pandas as pd

data = {
    "Instance": ["EC2-1", "EC2-2", "EC2-3"],
    "Team": ["DevOps", "Backend", "DevOps"],
    "CPU": [70, 50, 90]
}

df = pd.DataFrame(data)

summary = df.groupby("Team")["CPU"].aggregate(["mean","max"])

summary = summary.reset_index()

print(summary)

summary.to_csv("Summary.csv",index=False)

print("\nSummary File created : Summary.csv")