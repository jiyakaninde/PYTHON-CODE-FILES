class Student:
    Grade=13
    Name="Jiya"
    def intro(self):
        print("Introduction")
    def display(self):
        print("My name is ",self.Name)
        print("My grade is ", self.Grade)
s1=Student()
s1.intro()
s1.display()