#Day 53 – Polymorphism (Same Action, Different Behavior)
"""
Today you'll learn one of the coolest OOP concepts:

🎯 Polymorphism

Big word 😄

But after today's lesson, you'll understand it easily."""


#Example With Polymorphism

class EC2:
    def start(self):
        print("Ec2 Started..")

class RDS:
    def start(self):
        print("RDS Started..")


compute = EC2()

storage = RDS()

"""compute.start()
storage.start()"""


#🔥 6. Loop With Polymorphism
"""
Now the real magic:"""

starter = [
    EC2(),
    RDS()
]

for instance in starter:
    instance.start()

#🔥 8. Polymorphism + Inheritance

#Parent:

class CloudResource:
    def status(self):
        print("Resource Starting..")


#Child Classes

class EC2(CloudResource):
    def status(self):
        print("EC2 is Starting..")

    
class RDS(CloudResource):
    def status(self):
        print("RDS is Starting..")


resources = [
    EC2(),
    RDS()
]

for resource in resources:
    resource.status()