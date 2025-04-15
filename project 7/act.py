listofnum=[1,3,5,7,9]
judge=listofnum[2]
var1=int(input("guess the number the judge chose from(1,3,5,7,9)!!!"))
if(var1<judge):
    print("your guess was below the number chosen")
elif(var1==judge):
    print("CORRECTTTT BUZZZ BUZZZZ BUZZZ")
else:
    print("number was higher than the one picked")