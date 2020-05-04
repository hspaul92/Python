#Solution:1 Using inbuilt subset() method
def checkMultipleKeysInDict(d):
    l=eval(input("Enter List Of Elements You Want To Find In Dictionary Keys:"))                 
    print("Check if all Elements are in Dictionary keys ???",set(l).issubset(d.keys()))

dic ={2001:'AWS',2002:'Apple',2003:'Google'}
print("Original Dictionary:",dic)
checkMultipleKeysInDict(dic)                

#Solution:2  Usings comparison operater
def checkMultipleKeysInDict2(d):
    l=eval(input("Enter List Of Elements You Want To Find In Dictionary Keys:"))                 
    print("Check if all Elements are in Dictionary keys ???",d.keys() >= set(l))

dic ={2001:'AWS',2002:'Apple',2003:'Google'}
print("Original Dictionary:",dic)
checkMultipleKeysInDict2(dic)
