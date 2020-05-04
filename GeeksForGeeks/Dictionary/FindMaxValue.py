#Solution:1  Using max(values) and dict comprehension
def keyWithMaxValue1(d):
    v_max  = max(d.values())       
    x = {k:v for k,v in d.items() if v ==v_max }

    print("Key With Max Value:",x)

dic={'Audi':100, 'BMW':1292, 'Aston': 210000, 'Hyundai' : 88}
print("Dictionary    :",dic)
keyWithMaxValue1(dic)


#Solution:2  Using max(values) with key
def keyWithMaxValue2(d):
    m = max(d.items() , key= lambda x:x[1])
    print("Key With Max Value:",m)

dic={'Audi':100, 'BMW':1292, 'Aston': 210000, 'Hyundai' : 88}
print("Dictionary    :",dic)
keyWithMaxValue2(dic)
    
    
#Solution:3 Using max(values) with itemgetter() function
from operator import itemgetter
def keyWithMaxValue3(d):
    m = max(d.items() , key= itemgetter(1))
    print("Key With Max Value:",m)

dic={'Audi':100, 'BMW':1292, 'Aston': 210000, 'Hyundai' : 88}
print("Dictionary    :",dic)
keyWithMaxValue3(dic)


#Solution:4 Long way using inbuilt max(values) with index() function 
def keyWithMaxValue4(d):
    key= d.keys()
    value= d.values()    
    v_max  = max(value)
    x  = list(value).index(v_max)
    v = list(key)[x]
    m =(v,d[v])  
    print("Key With Max Value:",m)

dic={'Audi':100, 'BMW':1292, 'Aston': 210000, 'Hyundai' : 88}
print("Dictionary    :",dic)
keyWithMaxValue4(dic)
    
    
    
