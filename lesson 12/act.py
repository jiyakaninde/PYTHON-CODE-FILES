class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a dog, my name is {self.name} and i am {self.age} years old")
    def make_sound(self):
        print("woof")
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat, my name is {self.name} and i am {self.age} years old")
    def make_sound(self):
        print("meow")
        
cat1=cat("snickerdoodle","2")
cat1.info()
cat1.make_sound()
dog1=dog("weebles","0.5")
dog1.info()
dog1.make_sound()