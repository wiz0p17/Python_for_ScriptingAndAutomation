#“Employee Skill Filter”
"""
It should:

create DataFrame
filter Python users
export filtered CSV"""

import pandas as pd

data = {
    "Name": ["Vivek", "Neha", "Aman"],
    "Skill": ["Python", "Frontend", "Python"]
}

df = pd.DataFrame(data)

print(df)
print("*"*70)

pythonUsers = df[ df["Skill"] == "Python" ]

pythonUsers.to_csv("PythonUsers.csv",index=False)

print(pythonUsers)

print("\nFile Created with name: PythonUsers.csv\n")