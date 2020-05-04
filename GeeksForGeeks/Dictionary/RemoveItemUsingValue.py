#Solution:1 Using del() function
def removeItemUsingValue(d):
    print("Before Remove:",d)         
    v = input("Enter Element You Want To Remove:")
    if v  not in d.values():
       print("Specified Item is not present in dictonary !!!")
    else:
       for key,value in d.items():
           if value==v:
              del d[key]
              break
    print("After Remove:",d)
    
dic1 ={2001:'Apple',2002:'Samsung',2003:'Sony',2004:'Huwaie'}
removeItemUsingValue(dic1)

#Solution:2  Using pop() function
def removeItemUsingValue2(d):
    print("Before Remove:",d)         
    v = input("Enter Element You Want To Remove:")
    if v  not in d.values():
       print("Specified Item is not present in dictonary !!!")
    else:
       for key,value in d.items():
           if value==v:
              d.pop(key)
              break
    print("After Remove:",d)

dic1 ={2001:'Apple',2002:'Samsung',2003:'Sony',2004:'Huwaie'}
removeItemUsingValue2(dic1)


#Note: Problem With Above approach
#---------------------------------
#Here We are removing given key,value pair while executing iteration.
#So once item removed we need to come out of iteration using 'break'.
#The reason is here once the item removed the size of dictionary chaged
#in between iteration.So it will give runtime exception as below.
#     'RuntimeError: dictionary changed size during iteration'
#So Above two approach won't work if dictionary has more than one same values.


#Solution:3

def removeItemUsingValue2(d):
    print("Before Remove:",d)         
    v = input("Enter Element You Want To Remove:")
    if v  not in d.values():
       print("Specified Item is not present in dictonary !!!")
    else:
       result ={ x:y for x,y in d.items() if y != v}
    print("After Remove:",result)

dic1 ={2001:'Apple',2002:'Samsung',2003:'Sony',2004:'Huwaie'}
removeItemUsingValue2(dic1)

dic2 ={2001:'Apple',2002:'Samsung',2003:'Sony',2004:'Huwaie',2005:'Sony'}
removeItemUsingValue2(dic2)





