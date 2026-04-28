#“Secure CLI Tool”

'''It should:

Take:
--name
Read from .env:
API_KEY
Print both'''


import argparse
import os
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument("--name",required=True)

args = parser.parse_args()

api_key = os.environ.get("API_KEY")

print("Name :",args.name)
print("From api key :",api_key)

