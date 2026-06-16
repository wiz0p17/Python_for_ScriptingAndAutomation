#Assignment
"""Log Analyzer

Requirements:

Read:
logs.log
Count:
INFO
WARNING
ERROR
Create:
analysis_report.txt
Store:
INFO: X
WARNING: Y
ERROR: Z"""

info = 0
error = 0
warning = 0

with open("logs.log","r") as file:
    for line in file:
        if "INFO" in line:
            info += 1
        
        elif "WARNING" in line:
            warning += 1

        elif "ERROR" in line:
            error += 1
        
summary = f"""
LOG ANALYZER REPORT

info = {info}

warning = {warning}

errors = {error}

"""

with open("report.txt","w") as file:
    file.write(summary)
    
print("Report Generated")