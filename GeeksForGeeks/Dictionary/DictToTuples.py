#Solution :1 Using item function of dictionary
def dictToListOfTuple(d):
    t = list(d.items())
    print("List Of Tupples:",t)

dic ={2001:'Amazon',2001:'Apple',2002:'Google',2003:'Sony'}
dictToListOfTuple(dic)


#Solution:2 uisng String comprehesion 
def dictToListOfTuple2(d):
    t = [(k,v)for k,v in d.items()]
    print("List Of Tupples:",t)

dic ={2001:'Amazon',2001:'Apple',2002:'Google',2003:'Sony'}
dictToListOfTuple2(dic)
    
#Solution:3 using list append method
def dictToListOfTuple3(d):
    l= []
    for x,v in d.items():
        l.append((x,d[x]))
    print("List Of Tupples:",l)    

dic ={2001:'Amazon',2001:'Apple',2002:'Google',2003:'Sony'}
dictToListOfTuple3(dic)


#Solution4:using zip
def dictToListOfTuple4(d):
    k= d.keys()
    v= d.values()
    t= list(zip(k,v))
    print("List Of Tupples:",t)    

dic ={2001:'Amazon',2001:'Apple',2002:'Google',2003:'Sony'}
dictToListOfTuple4(dic)


#Solution4:using iteration
def dictToListOfTuple5(d):
    l =[]
    for x in d.keys():
        t = (x,d[x])
        l.append(t)
    print("List Of Tupples:",l)
    
dic ={2001:'Amazon',2001:'Apple',2002:'Google',2003:'Sony'}
dictToListOfTuple5(dic)    








