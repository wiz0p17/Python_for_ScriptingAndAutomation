#📅 Day 45 – Advanced Charts & Dashboard Styling
"""
From your roadmap :

✅ Improve visualizations
✅ Create multiple plots
✅ Build monitoring-style dashboards"""
""""
import pandas as pd 
import matplotlib.pyplot as plt


data = {
    "Instance": ["EC2-1", "EC2-2", "EC2-3"],
    "CPU": [70, 50, 90],
    "Memory": [60, 80, 75]
}


df = pd.DataFrame(data)

plt.figure(figsize=(10,5))

#CPU chart

plt.subplot(1,2,1)

plt.bar(df["Instance"],df["CPU"],color="orange" )

plt.title("CPU Chart")
plt.grid(True)


#Memory Chart

plt.subplot(1,2,2)

plt.bar(df["Instance"],df["Memory"],color="green")

plt.title("Memory Chart")

plt.grid(True)

plt.show()
"""


#📏 6. figsize (IMPORTANT)
"""
plt.figure(figsize=(10, 5))

Controls:

width
height

Like resizing image frame 🖼️"""

#8. Add Colors
"""
plt.bar(df["Instance"], df["CPU"], color="orange")"""


#📈 9. Line Monitoring Graph
"""
Perfect for:

CPU over time
network traffic
cloud metrics"""
"""
import pandas as pd 
import matplotlib.pyplot as plt

time = [1, 2, 3, 4]
cpu = [30, 50, 70, 60]

plt.plot(time,cpu)

plt.title("CPU over time")

plt.xlabel("Time")
plt.ylabel("CPU %")
plt.grid(True)

plt.show()"""


#🔥 11. Full Dashboard Example
"""
import matplotlib.pyplot as plt

import pandas as pd

data = {
    "Instance": ["EC2-1", "EC2-2", "EC2-3"],
    "CPU": [70, 50, 90],
    "Memory": [60, 80, 75]
}


df = pd.DataFrame(data)


plt.figure(figsize=(10,6))

#CPU Chart

plt.subplot(1,2,1)

plt.bar(df["Instance"],df["CPU"],color = "green")

plt.title("CPU Chart")
plt.grid(True)

#Memory Chart
plt.subplot(1,2,2)

plt.bar(df["Instance"],df["Memory"],color = 'orange')

plt.title("Memory Chart")

plt.grid(True)

plt.show()"""


# 12. Mini Practice (DO THIS)
"""
👉 Create:

CPU line graph
Memory bar graph

in same dashboard."""

import matplotlib.pyplot as plt

import pandas as pd

data = {
    "Instance": ["EC2-1", "EC2-2", "EC2-3"],
    "CPU": [70, 50, 90],
    "Memory": [60, 80, 75]
}


df = pd.DataFrame(data)


plt.figure(figsize=(10,6))

#CPU Chart

plt.subplot(1,2,1)

plt.plot(df["Instance"],df["CPU"],color = "green")

plt.title("CPU Chart")
plt.grid(True)

#Memory Chart
plt.subplot(1,2,2)

plt.bar(df["Instance"],df["Memory"],color = 'orange')

plt.title("Memory Chart")

plt.grid(True)

plt.show()