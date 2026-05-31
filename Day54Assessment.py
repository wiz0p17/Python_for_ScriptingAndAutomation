#Secure Cloud Server
"""
Attributes: __cpu
            __memory

Methods:    set_cpu()
            set_memory()

            get_cpu()
            get_memory()

Rules: 0–100 only"""

class Server:
    def __init__(self):
        self.__cpu = 0
        self.__memory = 0
    
    def set_cpu(self,cpu):
        if 0 <= cpu <= 100:
            self.__cpu = cpu
            
    @property
    def get_cpu(self):
        return self.__cpu
    
    def set_memory(self,memory):
        if 0 <= memory <= 100:
            self.__memory = memory

    @property
    def get_memory(self):
        return self.__memory
    
instance = Server()

instance.set_cpu(56)
instance.set_memory(67)

print(instance.get_cpu)
print(instance.get_memory)
