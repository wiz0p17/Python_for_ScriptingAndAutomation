#“Cloud Monitoring Dashboard”
"""
Create DataFrame:

Instance	CPU
EC2-1	    70
EC2-2	    50
EC2-3	    90

Your tool should:

create bar chart
show CPU comparison
save chart image"""


import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Instance": ["EC2-1", "EC2-2", "EC2-3"],
    "CPU": [70, 50, 90]
}

df = pd.DataFrame(data)

plt.bar(df["Instance"],df["CPU"])

plt.title("Cloud Monitoring Dashboard")

plt.xlabel("Instance")

plt.ylabel("CPU Utilization")

plt.show()