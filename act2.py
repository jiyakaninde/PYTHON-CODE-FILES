dict={"Name":"Jiya","Grade":12,"Age":17,"height":"155cm"}
print(dict)
#add
dict["Hobby"]="Art"
print(dict)
#update
dict["Grade"]=13
print(dict)
#poppp
dict.pop("height")
print(dict)
#getting
d=dict.get("Name")
print(d)
#clearing
dict.clear()
print(dict)