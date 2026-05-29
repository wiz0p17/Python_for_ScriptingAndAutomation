#🎯 Inheritance
"""
This is how real software systems avoid writing the same code again and again.

Used in:

AWS SDKs ☁️
Django 🌐
Flask APIs 🚀
Enterprise software 🏢
🧠 1. Easy Real-Life Analogy

Imagine a family 👨‍👩‍👦

Father has:

eyes
nose
hair

Son automatically inherits many of those traits.

Parent → Child

Same in Python:

Server
   ↓
EC2Server"""


#⚙️ 3. Parent Class
"""
class Server:
    def __init__(self,name):
        self.name = name
    
    def start(self):
        print(f"{self.name} Server Started")

class ec2Server(Server):
    def deploy(self):
        print(f"Deploying Servers on {self.name}")

server = ec2Server("Ec3Server")
server.start()
server.deploy()"""
"""
class CloudResources:
    def __init__(self,name):
        self.name = name


class Ec2(CloudResources):
    def start(self):
        print(f"Server started {self.name}")

class S3(CloudResources):
    def upload(self):
        print(f"Uploading Files on {self.name}")


Ec2_1 = Ec2("Amazon linux")
s3_s = S3("Parshuram")

Ec2_1.start()
s3_s.upload()"""


#🔥 9. Full Example

class Server:
    def __init__(self,name):
        self.name = name

    def start(self):
        print(f"{self.name} Started")

class EC2Server(Server):
    def __init__(self, name,cpu):
        super().__init__(name)

        self.cpu = cpu

    def showCPU(self):
        print(f"CPU Utilization : {self.cpu}%")


server = EC2Server("ecc2","79")

server.start()
server.showCPU()