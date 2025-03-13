weight=float(input("Enter your weight in KG"))
height=float(input("enter your height in CM"))
BMI= weight/(height/100)**2
print(BMI)
if BMI<=18.5:
    print("underweight")
elif BMI<=24.9:
    print("normal")
elif BMI<=29.9:
    print("overweight")
elif BMI<=34.9:
    print("obese")
else:
    print("extremely obese")
 