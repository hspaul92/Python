#Solution:1  Using dictionary comprehension
def swappingKeyValues(d):
    sd = {v:k for k,v in d.items()}
    print('After Swapping:',sd)
    
dic1 = {2001:'AWS',2002:'Google',2003:'Apple'}
print('Before Swapping:',dic1)
swappingKeyValues(dic1)
dic2 = {2001:'AWS',2002:'Google',2003:'AWS'}
swappingKeyValues(dic2)

#Solution:2  Using lambda expression
def swappingKeyValues2(d):
    sd = dict(map(reversed, d.items())) 
    print('After Swapping:',sd)

dic3 = {2001:'AWS',2002:'Google',2003:'Apple'}
print('Before Swapping:',dic3)    
swappingKeyValues2(dic3)

#Solution:3 Using key() , value(), zip()
def swappingKeyValues3(d):
    key=d.keys()
    value=d.values()
    sd=zip(value,key)
    print('After Swapping:',dict(sd))

dic3 = {2001:'AWS',2002:'Google',2003:'Apple'}
print('Before Swapping:',dic3)    
swappingKeyValues3(dic3)

dic31 = {2001:'AWS',2002:'Google',2003:'AWS'}
print('Before Swapping:>>>>>',dic31)    
swappingKeyValues3(dic31)


#Note
#----
#Above All three solution does not perform well when value got repeted
#All three version will store only latest kev:value combination
#To handle this special scenario , below solution is suggested


#Solution:4 Using Append method 
def swappingKeyValues4(d):
    new_dic ={}
    for k,v in d.items():
        if v in new_dic:
           new_dic[v].append(k)
        else:
           new_dic[v]=[k]
    print('After Swapping:',dict(new_dic))

dic4 = {2001:'AWS',2002:'Google',2003:'Apple'}
print('Before Swapping:',dic4)    
swappingKeyValues4(dic4)

dic5 = {2001:'AWS',2002:'Google',2003:'AWS'}
print('Before Swapping:',dic5)    
swappingKeyValues4(dic5)
