#4. First Abstract Class

from abc import ABC, abstractmethod
"""
class CloudResource(ABC):

    @abstractmethod
    def start(self):
        pass
"""

#⚡ Create Child Class
"""
class EC2(CloudResource):
    def start(self):
        print("EC2 Started...")

    
server = EC2()
server.start()"""


#🔥 8. Full Example

"""
from abc import ABC, abstractmethod

class MonitoringService(ABC):

    @abstractmethod
    def check_health(self):
        pass


class EC2Monitor(MonitoringService):

    def check_health(self):

        print("EC2 Healthy")


class RDSMonitor(MonitoringService):

    def check_health(self):

        print("Database Healthy")


services = [
    EC2Monitor(),
    RDSMonitor()
]

for service in services:

    service.check_health()"""



