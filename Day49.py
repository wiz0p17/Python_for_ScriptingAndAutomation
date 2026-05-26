#📅 Day 49 – Scheduling Automation
"""
From your roadmap :

✅ Understand cron jobs
✅ Schedule scripts
✅ Learn periodic automation
✅ Background execution concepts"""

"""
⚙️ 3. Cron Job Format
* * * * * command

Looks scary 😄
But it’s easy.

📦 4. Understanding Cron Fields
* * * * *
| | | | |
| | | | └── Day of week
| | | └──── Month
| | └────── Day
| └──────── Hour
└────────── Minute
🧠 Easy Example
0 9 * * * python report.py

Meaning:
👉 run every day at 9:00 AM ⏰

🔥 5. Common Cron Examples
Every minute
* * * * * python app.py
Every hour
0 * * * * python app.py
Daily at midnight
0 0 * * * python backup.py
"""


"""➕ 7. Add Cron Job

Example:

*/5 * * * * python3 /home/vivek/monitor.py

Meaning:
👉 run every 5 minutes 🔄

🧠 Easy Understanding
*/5

⚙️ 6. Open Cron Editor

Linux/Mac:

crontab -e

means:
👉 repeat every 5 units"""

print("Automation Running...\n")
