def findKeys(d,l):
    d2 = {x:d[x] for x in l if x in d.keys()}
    print(d2)

dic ={2001:'Apple',2002:'Amazon',2003:'Google',2004:'Sony'}
print("Original Dictionary :",dic)
lis = eval(input("Enter List Of Years You Want Find:"))
findKeys(dic,lis)

    
