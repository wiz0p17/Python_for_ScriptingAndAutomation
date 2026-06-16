#Log File Analysis with Python
"""
This is one of the most practical skills for:

☁️ Cloud Engineers
⚙️ DevOps Engineers
🔍 SREs (Site Reliability Engineers)"""
"""
with open("logs.log") as file:
    for line in file:
        print(line.strip())
"""

#Find Errors

with open("logs.log") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())

#count errors

error_count = 0

with open("logs.log") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        
print(f"Total Error: {error_count}")



"""info = 0
warning = 0
error = 0

with open("app.log") as file:

    for line in file:

        if "INFO" in line:
            info += 1

        elif "WARNING" in line:
            warning += 1

        elif "ERROR" in line:
            error += 1

print(f"INFO: {info}")
print(f"WARNING: {warning}")
print(f"ERROR: {error}")"""


#Generate Summary Report:

info = 33
warning = 4
error = 1

summary = f"""
Logs Analysis Report

INFO: {info}
WARNING: {warning}
ERROR: {error}

"""

with open("report.txt","w") as file:
    file.write(summary)





