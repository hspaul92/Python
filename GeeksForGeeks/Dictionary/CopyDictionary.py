#Solution:1 Using inbuilt copy() method
def copyDict(d):
    d1 = d.copy()
    print("New Dictionary:",d1)
    print("Address Of New Dictionary:",id(d1))
    

dic ={2001:'AWS',2002:'Apple',2003:'Google'}
print("Original Dictionary:",dic)
print("Address Of Original Dictionary:",id(dic))
copyDict(dic)


#Solution:2 Using dict comprehesion
def copyDict2(d):
    d2 = {x:v for x,y in d.items()}
    print("New Dictionary:",d2)
    print("Address Of New Dictionary:",id(d2))    

dic2 ={2001:'AWS',2002:'Apple',2003:'Google'}
print("Original Dictionary:",dic2)
print("Address Of Original Dictionary:",id(dic2))
copyDict(dic2)


#Solution:3 Using inbuit dict()
def copyDict(d):
    d3 = dict(d)
    print("New Dictionary:",d3)
    print("Address Of New Dictionary:",id(d3))   

dic3 ={2001:'AWS',2002:'Apple',2003:'Google'}
print("Original Dictionary:",dic3)
print("Address Of Original Dictionary:",id(dic3))
copyDict(dic3)

