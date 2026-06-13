#Assignment (Cloud Engineer Version)

"""Build: Config Reader

Read:

APP_ENV
AWS_REGION
PROJECT_NAME

Using:

os.getenv()

Print:

Environment: dev
Region: ap-south-1
Project: CloudMonitor"""

import os 

environ = os.getenv("APP_ENV","DEV")
region = os.getenv("AWS_REGION","ap-south-1")
projectName = os.getenv("PROJECT_NAME","COC")

print(environ)
print(region)
print(projectName)

