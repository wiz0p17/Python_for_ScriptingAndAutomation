#📅 Day 43 – Grouping Data & Generating Summaries
"""
From your roadmap :

✅ Group data
✅ Generate summaries
✅ Perform aggregations
✅ Build analytics reports"""

"""import pandas as pd

data = {
    "Name": ["Vivek", "Neha", "Aman"],
    "Department": ["Cloud", "Frontend", "Cloud"],
    "Marks": [90, 75, 95]
}

df = pd.DataFrame(data)
print(df)
print("\n","*"*50)
"""
#🔥 3. Group Data (groupby)
"""
grouped = df.groupby("Department")
"""

#📊 4. Calculate Average
"""
average_marks = df.groupby("Department")["Marks"].mean()

print(average_marks)
print("\n","*"*50)
"""

#🔥 5. Count Values

#👉 Count students per department:
"""
count = df.groupby("Department")["Name"].count()

print(count)
print("\n","*"*50)
"""

#📈 6. Multiple Aggregations
"""
summary = df.groupby("Department")["Marks"].aggregate(["mean","min","max"])

summary = summary.reset_index()

print(summary)
print("\n","*"*50)


summary.to_csv("Summary.csv",index=False)

print("Data is written in: Summary.csv")
"""


#🔥 9. Full Workflow Example

import pandas as pd

data = {
    "Name": ["Vivek", "Neha", "Aman", "Rahul"],
    "Department": ["Cloud", "Frontend", "Cloud", "Frontend"],
    "Marks": [90, 75, 95, 80]
}

df = pd.DataFrame(data)

summary = df.groupby("Department")["Marks"].aggregate(["mean","min","max"])

summary = summary.reset_index()

summary.to_csv("Summary.csv",index=False)

print(summary)

print("File created of summary: Summary.csv")


#🧪 10. Mini Practice (DO THIS)
"""
👉 Find: highest marks by department"""


topper = df.groupby("Department")["Marks"].aggregate("max")
print(topper)