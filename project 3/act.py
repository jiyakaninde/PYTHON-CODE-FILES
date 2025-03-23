var1=int(input("Enter number of working days: "))
var2=int(input("Enter number of absent days: "))

per=(var2/var1)*100

if(per<=75):
    print("You will not be able to sit for exams")
else:
    print("You will be able to sit for exams")