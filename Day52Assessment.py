#Cloud Resource System
"""
Parent Class:

CloudResource

Attributes:

name

Method:

info()"""


class CloudResources:
    def __init__(self,name):
        self.name = name
    
    def info(self):
        print(f"Resource: {self.name}")


class Ec2(CloudResources):
    def start(self):
        print(f"Server started {self.name}")

class S3(CloudResources):
    def upload(self):
        print(f"Uploading Files on {self.name}")


Ec2_1 = Ec2("Amazon linux")
s3_s = S3("Parshuram")

Ec2_1.info()
Ec2_1.start()

s3_s.info()
s3_s.upload()
