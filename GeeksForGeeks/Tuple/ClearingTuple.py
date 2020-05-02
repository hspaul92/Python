# Solution: 1 Using inbuilt clear() method of list
def clearTheTuple1(t):
    l =list(t)
    l.clear()
    print("Using Solution1: After Clearing, Tuple Conatains ",len(l) ," elements")


# Solution: 2 By reinitializing tuple
def clearTheTuple2(t):
    t=()
    print("Using Solution2 :After Clearing, Tuple Conatains ",len(t) ," elements")


t = (2002,2001,2004,2005,2003)
print("Input tuple: ",t)

#Using Solution:1
clearTheTuple1(t)

#Using solution:2
clearTheTuple2(t)
