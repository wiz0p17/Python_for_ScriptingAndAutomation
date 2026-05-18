#📅 Day 41 – Pandas Basics
"""
From your roadmap :

✅ Learn pandas basics
✅ Read CSV easily
✅ Filter & analyze data"""


#📊 4. Create First DataFrame
"""
import pandas as pd

data = {
    "name": ["Vivek","Neha"],
    "Skill": ["Python","Frontend"]
}

df = pd.DataFrame(data)

print(df)"""


#📄 6. Read CSV File (SUPER IMPORTANT 🔥)
"""
import pandas as pd

df = pd.read_csv("user.csv")

print(df)"""

#Access Column
"""
print(df["Name"][0])
"""

#📌 Access Specific Row
"""
print(df.iloc[1])
"""

#🎯 8. Filter Data (VERY IMPORTANT)
"""
python_users = df[df["Skill"] == "Python"]

print(python_users)"""


#✍️ 9. Export CSV
"""
python_users.to_csv("pythonUsers.csv",index=False)
"""

#🔥 10. Full Pandas Workflow
"""
import pandas as pd

data = {
    "Name": ["Neha","Vivek","Random"],
    "Skill": ["Frontend","Python","Python"]
}

df = pd.DataFrame(data)

print(df)
print("-"*50)

pythonSkills = df[ df["Skill"] == "Python" ]

print(pythonSkills)

pythonSkills.to_csv("PythonUsers.csv",index=False)

print("\nFile Created PythonUsers.csv\n")
"""

#🧪 11. Mini Practice (DO THIS)

#👉 Create DataFrame:

import pandas as pd

data = {
    "Cloud" : ["AWS","Azure","GCP"],
    "Languages": ["Python","Java","C++"]
}

df = pd.DataFrame(data)

print(df)