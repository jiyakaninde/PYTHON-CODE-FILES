class area:
    def __init__(self,area):
        self.area=area
    def display(self):
        print("the area of the trapeziod is ",self.long_base**self.short_base**self.height**0.5)
class trapeziod:
    def __init__(self,long_base,short_base,height):
        self.long_base=long_base
        self.short_base=short_base
        self.height=height
        area.__init__(self,area)
    def display1(self):
        print("the long base is ", self.long_base)
        print("the short base is ",self.short_base)
        print("the height is ",self.height)
        area.display(self)
ob=trapeziod(3,2,1)
ob.display1()
