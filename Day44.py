#📅 Day 44 – Introduction to Data Visualization
"""
From your roadmap :

✅ Create graphs
✅ Visualize reports
✅ Understand plotting basics"""

"""
import matplotlib.pyplot as plt

marks = [70,90,80]

plt.plot(marks)

plt.show()"""


#🔥 5. Add Labels
"""
import matplotlib.pyplot as plt

students = ["Vivek","Neha","Rajat"]
marks = [89,95,85]

plt.plot(students,marks)

plt.title("Students Marks")

plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
"""

#📊 6. Bar Chart (VERY IMPORTANT)
"""
import matplotlib.pyplot as plt

students = ["Neha","Vivek","Rajat"]
marks = [89,92,80]

plt.bar(students,marks)

plt.title("Students Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()
"""


#🥧 7. Pie Chart
"""
import matplotlib.pyplot as plt

services = ["AWS","Azure","GCP"]
percentage = [55,25,20]

plt.pie(percentage,labels=services)

plt.title("Cloud Service Provider")

plt.show()"""

#📉 8. Save Graph as Image
"""
plt.savefig("CloudProvider.png")"""


#🔥 9. Full Example with Pandas

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Instance": ["EC2-1", "EC2-2", "EC2-3"],
    "CPU": [30, 85, 60]
}

df = pd.DataFrame(data)

plt.bar(df["Instance"], df["CPU"])

plt.title("EC2 CPU Usage")

plt.xlabel("Instance")
plt.ylabel("CPU")

plt.show()