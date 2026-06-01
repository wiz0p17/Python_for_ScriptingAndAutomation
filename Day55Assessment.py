#Cloud Deployment Framework
"""
Parent: CloudResource

Abstract methods:   deploy()
                    stop()

Children:   EC2
            Lambda"""

from abc import ABC, abstractmethod

class CloudResource(ABC):

    @abstractmethod
    def deploy(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Ec2Instance(CloudResource):
    def deploy(self):
        print("Deployed EC2 instance...")

    def stop(self):
        print("Stopped EC2 instance...")

class Lambda(CloudResource):
    def deploy(self):
        print("Deployed Lambda...")

    def stop(self):
        print("Stopped Lambda...")


server = [Ec2Instance(),Lambda()]

for i in server:
    i.deploy()
    i.stop()