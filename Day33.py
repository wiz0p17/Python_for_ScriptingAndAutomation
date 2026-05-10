#📅 Day 33 – CSV Files (csv module)
"""
From your roadmap :

✅ Read CSV files
✅ Write CSV reports
✅ Process structured tabular data"""

"""import csv

with open("employees.csv","r") as f:
    reader = csv.reader(f)
    
    for row in reader:
        print(row)"""


#🔥 3. Skip Header Row

"""import csv

with open("employees.csv","r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print("Name:", row[0])
        print("Department:", row[1])"""


#✍️ 5. Write CSV File

"""import csv

data = [
    ["name", "role"],
    ["Vivek", "Cloud Engineer"],
    ["Neha", "Frontend Developer"]
]

with open("output.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerows(data)

print("CSV written!")"""

"""⚠️ 6. Why newline=""?

Very important on Windows:
👉 Prevents blank lines between rows"""



#🔥 7. Dictionary-Based CSV (BEST PRACTICE)

"""
import csv

data = [
    {
        "name":"Vivek",
        "role":"Cloud"
    },
    {
        "name":"Neha",
        "role":"Frontend"
    }
]

with open("output.csv","w",newline="") as file:

    fields = ["name","role"]

    writer = csv.DictWriter(file,fieldnames=fields)

    writer.writeheader()
    writer.writerows(data)"""


#📌 Read Dict CSV
"""
import csv

with open("output.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"],row["role"])
"""

#👉 Create a CSV file:

import csv

with open("output.csv","w",newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Name","Role"])
    writer.writerow(["Vivek","Python"])


