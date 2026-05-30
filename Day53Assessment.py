#Cloud Monitoring System
"""
Parent: CloudResource

Method: check_health()

Children:   EC2
            RDS
            Lambda

Each should return different health messages."""


#Parent
class CloudResource:
    def check_health(self):
        print("Generic Health..")

#Inherited Child
class EC2(CloudResource):
    def check_health(self):
        print("EC2 Healthy")

class RDS(CloudResource):
    def check_health(self):
        print("RDS Healthy")

class Lambda(CloudResource):
    def check_health(self):
        print("Lambda Healthy")

resources = [
    EC2(),
    RDS(),
    Lambda()
]

for resource in resources:
    resource.check_health()