#“Cloud Inventory Analyzer”
"""
Create DataFrame:

Instance	CPU
EC2-1	    30
EC2-2	    85
EC2-3	    60

Your tool should:

filter CPU > 50
sort highest first
export CSV report"""


import pandas as pd

data = {
    "Instance" : ["EC2-1","EC2-2","EC2-3"],
    "CPU" : [30,60,85]
}

df = pd.DataFrame(data)

HighCPU = df[ df["CPU"] > 50 ]

sortedHighCPU = HighCPU.sort_values(by="CPU", ascending=False)

#write data to CSV

sortedHighCPU.to_csv("HighCPU.csv",index=False)

print("file created of Hight CPU : HighCPU.csv")
