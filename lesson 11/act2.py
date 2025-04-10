class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print("Person's full name is ", self.fname +" "+ self.lname)
class Student(Person):
    def __init__(self,fname,lname,year):
        self.year=year
        super().__init__(fname,lname)
    def display1(self):
        print("the graduation year is ",self.year)
        Person.display(self)
ob=Student("Jiya","Kaninde",2024)
ob.display1()