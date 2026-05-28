#📅 Day 51 – OOP Basics: Classes & Objects
"""
From your roadmap :

✅ Understand classes
✅ Create objects
✅ Learn methods & attributes
✅ Structure real applications"""

"""
class Student:
    pass

student1 = Student()

print(student1)"""


#👉 student can display marks.
"""
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


Student1 = Student("Vivek","58")

print(Student1.name)
print(Student1.marks)"""


#Example
"""
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    
    def show(self):
        print(
            f"{self.name} scored {self.marks}"
        )


Student1 = Student("Vivek","90")
Student1.show()"""


#🔥 9. Full Example

class Ec2Instance:
    def __init__(self,cpu,name):
        self.name = name
        self.cpu = cpu

    def show_status(self):
        print(
            f"{self.name} CPU usage:{self.cpu}%"
        )

server1 = Ec2Instance("EC2-1","78")
server2 = Ec2Instance("EC2-2","84")

server1.show_status()
server2.show_status()