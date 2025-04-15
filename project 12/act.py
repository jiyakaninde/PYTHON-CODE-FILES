class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print("my area is:", self.base**self.height**0.5)
class rectangle:
    def __init__(self,breath,length):
        self.breath=breath
        self.length=length
    def area(self):
        print("my area is :", self.breath**self.length)
class trapeziod:
    def __init__(self,long_base,short_base,height):
        self.long_base=long_base
        self.short_base=short_base
        self.height=height
    def area(self):
        print("my area is :", self.long_base**self.short_base**self.height**0.5)
        
tri=triangle(5,4)
rec=rectangle(3,5)
trap=trapeziod(6,3,2)

for shape in (tri,rec,trap):
    shape.area()