#Solution1: Using  dict compreshion and sorted() method
def sortListInsideDict(d):
    d ={ x:sorted(y) for x,y in d.items()}
    print("After Sort:",d)

dic ={ "L1":[87, 34, 56],"L2":[23, 00, 30], 
	"L3":[1, 6, 2], "L4":[40, 21] }
print("Before Sort:",dic)
sortListInsideDict(dic)


#Solution2: Using  sorted() method
def sortListInsideDict2(d):
    di ={}
    for x,y in d.items():
        di[x]=sorted(y)
    print("After Sort:",di)

dic2 ={ "L1":[87, 34, 56],"L2":[23, 00, 30], 
	"L3":[1, 6, 2], "L4":[40, 21] }
print("Before Sort:",dic2)
sortListInsideDict2(dic2)
    
