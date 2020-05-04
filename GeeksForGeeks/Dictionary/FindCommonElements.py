#Using iteration and membership operater

def commonElements(d1,d2):
    comm_dict={}
    for x,y in d1.items():
        if x in d2.keys():
           comm_dict[x]=y
    print(comm_dict)
    
dic1={1:'a',2:'b',3:'c'}
dic2={4:'d',5:'e',2:'b'}

commonElements(dic1,dic2)

#Uisng tiple and intersection operater

def commonElements2(d1,d2):
    comm_tuple= d1.items() & d2.items()    
    print(dict(comm_tuple))

dic1={1:'a',2:'b',3:'c'}
dic2={4:'d',5:'e',2:'e'}

commonElements2(dic1,dic2)
