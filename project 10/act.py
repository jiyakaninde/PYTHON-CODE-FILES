class numbers:
    def __init__(self,num1,num2,num3):
        self.num1=int(num1)
        self.num2=int(num2)
        self.num3=int(num3)
    def display(self):
        print("the sum of the numbers are ", self.num1 + self.num2 + self.num3)
obj=numbers(2,4,5)
obj.display()