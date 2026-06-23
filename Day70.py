from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def job():
    print("Hello Vivek")

scheduler.add_job(job,"interval",seconds = 5)

scheduler.start()

####
#1️⃣Trigger Types
####

#APScheduler supports 3 important trigger types.

#Interval trigger

"""Run repeatedly"""

scheduler.add_job(job,"interval",minutes = 1)

#2️⃣ Date Trigger

"""Run only once."""

scheduler.add_job(job,"date",run_date = "2026-07-01 08:00:00")

#3️⃣ Cron Trigger

"""Most powerful trigger."""

scheduler.add_job(job,"cron",hour = 8,minute = 0)

#Run daily at 8:00 AM


##Every monday 

scheduler.add_job(job,"cron",day_of_week = "mon")

##Every monday 8 AM

scheduler.add_job(job,"cron",day_of_week = "mon",hour = 8)

