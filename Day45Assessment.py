##🎯 13. Your Assignment (🔥 Important)
"""
👉 Build this:

“Mini CloudWatch Dashboard”

Your dashboard should show:

CPU chart
Memory chart
Save dashboard image"""


import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Instance": ["EC2-1", "EC2-2", "EC2-3"],
    "CPU": [70, 50, 90],
    "Memory": [60, 80, 75]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,5))


# cpu Chart 

plt.subplot(1,2,1)

plt.bar(df["Instance"],df["CPU"],color = "green")

plt.title("CPU Chart")

plt.grid(True)


#Memory Chart

plt.subplot(1,2,2)

plt.bar(df["Instance"],df["Memory"],color = "blue")

plt.title("Memory Chart")

plt.grid(True)

plt.show()