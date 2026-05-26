##“Daily Monitoring Automation”
"""
Your setup should:
✅ create monitoring script
✅ append logs
✅ prepare cron schedule"""


from datetime import datetime

log = f"{datetime.now()} Monitoring active\n"

with open("monitoring.log","a")as file:
    file.write(log)
