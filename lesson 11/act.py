class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print("The name of the person is ", self.name)
        print("The idnumber of the person is ", self.idnumber)
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)
    def display1(self):
        print("The salary is ", self.salary)
        print("the post is ",self.post)
        Person.display(self)
ob = Employee("jiya","012",1000000,"director")
ob.display1()