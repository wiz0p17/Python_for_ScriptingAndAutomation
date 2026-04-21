##Basic Logging Setup

import logging

'''logging.basicConfig(level=logging.INFO)

logging.info("This is information")
logging.warning("This is warning")
logging.error("This is error")'''

'''| Level    | Use               |
| -------- | ----------------- |
| DEBUG    | Detailed info     |
| INFO     | Normal events     |
| WARNING  | Something unusual |
| ERROR    | Something failed  |
| CRITICAL | Serious issue     |
'''


'''logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

logging.info("Script Started")'''


"""Replace print() with logging
❌ Before:
print("Deleting file:", file)
✅ After:
logging.info(f"Deleting file: {file}")"""



#Logging with Error Handling

'''import logging
from pathlib import Path

logging.basicConfig(filename="app.log",level=logging.INFO)

for file in Path(".").rglob("*"):
    if file.is_file():
        try:
            logging.info(f"Processing Files : {file}")
        
        except Exception as e:
            logging.info(f"Error with {file} : {e}")'''


###Logged File Cleaner

'''import logging
import time
from pathlib import Path

logging.basicConfig(filename="logs.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

currentTime = time.time()

for file in Path(".").rglob("*"):
    if file.is_file():
        try:
            age = currentTime - file.stat().st_mtime

            if age > 7 * 86400:
                logging.info(f"Deleting File: {file.name}")
                file.unlink
        except Exception as e:
            logging.info(f"An error occoured in {file.name} : {e}")'''



#👉 Create a log file and write:

import logging

logging.basicConfig(filename="xyz.log",level=logging.INFO)

logging.info("Program Started")
logging.warning("This is a warning")
logging.error("An error occoured")