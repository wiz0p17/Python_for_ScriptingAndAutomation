##📅 Day 21 – Environment Variables (os.environ & .env)

'''
✅ Use environment variables
✅ Avoid hardcoding sensitive data
✅ Make scripts configurable'''


##Access Environment Variables

'''import os

print(os.environ.get("HOME"))'''

import os

'''api_key = os.environ.get("API_KEY")

print(api_key)'''


##⚠️ 3. Safer Way (Avoid None)


'''import os 

api_key = os.environ.get("API_KEY","default_value");

print(api_key)'''

'''
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("API_KEY")

print(api_key)'''



#🔥 7. Real Automation Script

#👉 CLI + Environment Variable
'''
import argparse
from dotenv import load_dotenv
import os

load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument("--name",required=True, help="Add Name")

args = parser.parse_args()

api_key = os.environ.get("API_KEY")

print("Hello",args.name)
print("From api key :",api_key)'''




#🧪 8. Mini Practice (DO THIS)

from dotenv import load_dotenv
import os 

load_dotenv()

name = os.environ.get("USER_NAME")

print("Name :",name)



