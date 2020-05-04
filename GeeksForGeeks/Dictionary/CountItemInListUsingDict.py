#Solution:1 Using inbuilt count() method of List
def countItemInListUsingDict1(l):
    d={}
    for x in l:
        if x not in d:
           d[x]= l.count(x)
    print('Element Count:',d)

dic1 = [1,2,3,4,5,2,2,1,3,4,2,1,4]
print("Original List:",dic1)
countItemInListUsingDict1(dic1)


#Solution:2 Using inbuilt count() method of List
def countItemInListUsingDict2(l):
    d={}
    for x in l:
        if x in d:
           d[x]= d[x] + 1
        else:
           d[x]= 1           
    print('Element Count:',d)

dic2 = [1,2,3,4,5,2,2,1,3,4,2,1,4]
print("Original List:",dic2)
countItemInListUsingDict2(dic2)
