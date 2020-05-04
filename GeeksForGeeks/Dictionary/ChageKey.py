#using pop() method
def changeKeys(d):
    old_key = input("Enter Old Key You:")
    new_key = input("Enter New Key You:")
    print("Original Dictionary :",d)
    if old_key  not in d.keys():
       print ("Specified Old Key is not present")
    else:
       d[new_key]= d.pop(old_key)
       print("After change :",d)


dic= {'a':1,'b':2,'c':3,'d':4}
changeKeys(dic)



#using del() method
def changeKeys2(d):
    old_key = input("Enter Old Key You:")
    new_key = input("Enter New Key You:")
    print("Original Dictionary :",d)
    if old_key  not in d.keys():
       print ("Specified Old Key is not present")
    else:
       d[new_key]= d[old_key]
       del d[old_key]
       print("After change :",d)

dic= {'a':1,'b':2,'c':3,'d':4}
changeKeys2(dic)       
