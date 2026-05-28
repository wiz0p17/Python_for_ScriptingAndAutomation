#“Cloud Server Class”
"""
Your class should:
✅ store:

server name
CPU usage
memory usage

✅ method:

show_report()"""

class Server:

    def __init__(self,name,CPU,memory):
        self.name = name
        self.cpu = CPU
        self.memory = memory

    
    def show_report(self):
        print(
            f"{self.name} | "
            f"CPU usage: {self.cpu}% | "
            f"Memory: {self.memory}%"
        )

    
server1 = Server("Ec2-1","68","79")

server1.show_report()