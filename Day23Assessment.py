#“Config Manager Tool”
'''
It should:

Load .env
Validate:
API_KEY
APP_ENV
Print config safely'''


import os 
from dotenv import load_dotenv

load_dotenv()

required_vars = ["APP_ENV","API_KEY","LOG_LEVEL","TIMEOUT"]

for var in required_vars:
    if not os.getenv(var):
        raise ValueError(f"{var} is missing")
    
print("Config loaded Successfully!!")

print("Environment :",os.getenv(required_vars[0]))