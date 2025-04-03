class vehicle:
    vehiclename= "Range rover"
    def __init__(self,colour,type1):
        print("this method gets executed automatically")
        self.colour=colour
        self.type1=type1
    def display(self):
        print("the colour of this vehicle is ",self.colour)
        print("the type of vehicle is ",self.type1)
v1= vehicle("Black","Car")
v1.display()
print("the name of this vehicle is ", v1.vehiclename)