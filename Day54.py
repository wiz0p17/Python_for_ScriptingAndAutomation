#🎯 Encapsulation
"""
🎯 2. What is Encapsulation?

Encapsulation means:

Hide internal details
Control access to data

Think:

Mobile App
     ↓
Buttons Visible

Internal Code Hidden


🔒 5. Stronger Privacy

Use double underscore:"""


class BankAccount:
    def __init__(self):
        self.__balance = 10000
    
    """⚡ 6. Getter Method

    Getter = read data safely."""
    def getBalance(self):
        return self.__balance
    
    """⚡ 7. Setter Method

    Setter = update data safely."""
    def setBalance(self,amount):
        if amount >=0:
            self.__balance = amount


account = BankAccount()

account.setBalance(50000)
print(account.getBalance())


#🔥 9. Full Cloud Example

class EC2Instance:
    def __init__(self):
        self.__cpu = 0
    @property
    def setCpu(self,cpu):
        if 0 <= cpu <=100:
            self.__cpu = cpu
        
    def getCpu(self):
        return self.__cpu
    
instance = EC2Instance()

instance.setCpu(56)

print(instance.getCpu())

