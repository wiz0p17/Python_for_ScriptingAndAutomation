#📅 Day 42 – Advanced Pandas Operations
"""
From your roadmap :

✅ Sort data
✅ Filter advanced conditions
✅ Handle missing values
✅ Generate statistics"""

"""
import pandas as pd

data = {
    "Name": ["Vivek","Neha","Chaman"],
    "Marks": [85,90,75]
}
print("\n","*"*60)
df = pd.DataFrame(data)

print(df)"""

#🔍 3. Filter Data (VERY IMPORTANT)
"""
👉 Students above 80:"""
"""
high_scores = df[df["Marks"] > 80]
print("\n","*"*60)
print(high_scores)

filtered = df[
    (df["Marks"]>80) &
    (df["Name"] == "Vivek")
]
print("\n","*"*60)
print(filtered)"""

#📊 5. Sorting Data

#👉 Highest marks first:
"""
sorted_DF = df.sort_values(by="Marks",ascending=False)

print("\n","*"*60)
print(sorted_DF)"""


#📈 6. Basic Statistics (SUPER IMPORTANT 🔥)

##👉 Average:
"""
print(df["Marks"].mean())

#👉 Maximum:
print(df["Marks"].max())

#👉 Minimum:
print(df["Marks"].min())
"""

#📦 7. Describe Entire Data
"""
print(df.describe())"""


#⚠️ 8. Missing Values (VERY IMPORTANT)

#Real data often has empty values.
"""
data1 = {
    "Name": ["Vivek", "Neha", None],
    "Marks": [90, None, 95]
}

df1 = pd.DataFrame(data1)"""

#🔍 Check Missing Values
"""
print(df1.isnull())"""

#🧹 Remove Missing Rows
"""
cleaned = df1.dropna()

print(cleaned)"""


#🔄 Fill Missing Values
"""
df1["Marks"] = df1["Marks"].fillna(0)

print(df1)"""


#🔥 9. Full Workflow Example

import pandas as pd 

data = {
    "Name" : ["Vivek","Neha","Vinay"],
    "Marks" : [90,91,85]
}

df = pd.DataFrame(data)

Top_Students = df[ df["Marks"] >= 85 ]

sorted_Top_students = Top_Students.sort_values(by="Marks",ascending=False)

print(sorted_Top_students)

#write to CSV

sorted_Top_students.to_csv("Toppers.csv",index=False)

print("file created: Topper.csv")

#🧪 10. Mini Practice (DO THIS)
"""
👉 Find:
average marks
top scorer
"""

print("Average Marks = ",sorted_Top_students["Marks"].mean().__ceil__())
print("Top Scorer = ",sorted_Top_students["Marks"].max())