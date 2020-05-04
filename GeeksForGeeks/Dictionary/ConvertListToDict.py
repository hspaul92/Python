#Solution:1 Using compresheion
def convertListToDict1(k_list,v_list):

    if len(k_list)> len(v_list):
       for x in range(0,len(k_list)-len(v_list)):
           v_list.append('None')         
    d = {k_list[x]:v_list[x] for x in range(0,len(k_list))}
    print(d)

kl= [2001,2002,2003,2004,2007]
print("List One:",kl)
vl= ['Sony','Apple','AWS','Google']
print("List Two:",vl)

convertListToDict1(kl,vl)


#Solution:2 Using nested for loop
def convertListToDict2(k_list,v_list):
    d={}         

    if len(k_list)> len(v_list):
       for x in range(0,len(k_list)-len(v_list)):
           v_list.append('None')
    for x in k_list:
        for y in v_list:
            #print("key",x)
            #print("value",y)         
            d[x]=y
            v_list.remove(y)
            break
    print(d)

kl= [2001,2002,2003,2004,2007]
print("List One:",kl)
vl= ['Sony','Apple','AWS','Google']
print("List Two:",vl)

convertListToDict2(kl,vl)



#Solution:3 Using zip() method
def convertListToDict3(k_list,v_list):
    if len(k_list)> len(v_list):
       for x in range(0,len(k_list)-len(v_list)):
           v_list.append('None')

    d = dict(zip(k_list,v_list))
    print(d)


kl= [2001,2002,2003,2004,2007]
print("List One:",kl)
vl= ['Sony','Apple','AWS','Google']
print("List Two:",vl)
convertListToDict3(kl,vl)


