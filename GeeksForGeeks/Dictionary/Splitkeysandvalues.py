#Method:1
def keysAndValues(d):
    k= list(d.keys())
    v= list(d.values())
    print("Keys  :",k)
    print("Values:",v)

dic= {100:'Google',202:'Apple',300:'Amazon',400:'MS'}
print("original Keys:",dic)
keysAndValues(dic)


#Method:2
def keysAndValues2(d):
    k=[]
    v=[]
    for x,y in d.items():
        k.append(x)
        v.append(y)

    print("Keys  :",k)
    print("Values:",v)    
    
dic= {100:'Google',202:'Apple',300:'Amazon',400:'MS'}
print("original Keys:",dic)
keysAndValues2(dic)


#Method:3 Using Zip and Tupple Unpacking 
def keysAndValues3(d):
    z = zip(*d.items())
    k,v = tuple(z)
    keys= list(k)
    values=list(v)
    print("Keys  :",keys)
    print("Values:",values)

dic= {100:'Google',202:'Apple',300:'Amazon',400:'MS'}
print("original Keys:",dic)
keysAndValues3(dic)    


#Solution:4 Using itemgetter() function
from operator import itemgetter
def keysAndValues4(d):
    key = [itemgetter(0)(x) for x in d.items()]
    value = [itemgetter(1)(x) for x in d.items()]
    print("Keys  :",key)
    print("Values:",value)

dic= {100:'Google',202:'Apple',300:'Amazon',400:'MS'}
print("original Keys:",dic)
keysAndValues4(dic)  

    
     
