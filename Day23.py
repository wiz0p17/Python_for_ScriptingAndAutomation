##📅 Day 23 – Environment Variables (Best Practices & Real Usage)
'''
From your roadmap :

✅ Use .env properly
✅ Validate configs
✅ Structure environment-based setups
✅ Avoid common mistakes'''


'''import os
from dotenv import load_dotenv


load_dotenv()

app_env = os.getenv("APP_ENV")

apikey = os.getenv("API_KEY")

log = os.getenv("LOG_LEVEL")

timeout = int(os.getenv("TIMEOUT"))

print(app_env,"\n",apikey,"\n",log,"\n",type(timeout))'''

'''
import os 
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("API_KEY")

if not apikey:
    print("API key missing !!!")
else:
    print("Hello from api key",apikey)'''


'''from config import Config

Config.validate()

print(Config.API_KEY)
print(Config.APP_ENV)
print(Config.Timeout)'''



##🔥 7. Real Automation Script

from config import Config
import argparse

Config.validate()

parser = argparse.ArgumentParser()

parser.add_argument("--name",required=True)

args = parser.parse_args()

print("Hello",args.name)
print("API key loaded :",bool(Config.API_KEY))
print("Environment :",Config.APP_ENV)




