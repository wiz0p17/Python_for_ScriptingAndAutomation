#Day 64 – Environment Variables (os.environ)

#Today you're learning a skill used by every Cloud Engineer, DevOps Engineer, and Backend Developer.

import os

#dont use environ instead use getenv

#because if something does not exists environ gives error , unlike getenv


region = os.getenv("AWS_REGION","ap-south-1")

print(region)

#Set Environment Variable in Python

import os 

os.environ["APP_ENV"] = "development"

print(os.environ["APP_ENV"])

