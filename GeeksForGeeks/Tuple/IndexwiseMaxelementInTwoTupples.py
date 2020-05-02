# Case :
# Consider there are two tuples for two shop , contains price of three product P1,P2,P3
# like shop =(P1 price, P2 price ,P3 price)
# We need to find max price of each product . Ex:
# shop1 =(10, 4, 5)
# shop2 =(2, 5, 18)
# Max Price Of each product (10, 5, 18)

# Solution :1 Using iteration and append() method of list
def maxElementIntuple1(t1,t2):
    l = []
    for i in range (0,len(t1)):
        if t1[i] > t2[i]:
            l.append(t1[i])
        else:
            l.append(t2[i])
    print("Using Solution1:",tuple(l))

# Solution :2 Using list Comprehension
def maxElementIntuple2(t1,t2):
    l = [ t1[i] if t1[i]> t2[i] else t2[i]  for  i in range(0,len(t1))  ]
    print("Using Solution2:",tuple(l))

# Solution :3 Using map() with lambda function
def maxElementIntuple3(t1,t2):
    t = tuple(map(lambda i, j: max(i, j), t1, t2))
    print("Using Solution3:",tuple(t))

# Solution :4 Using map() with zip() function
def maxElementIntuple4(t1,t2):
    t = tuple(map(max,(zip(t1, t2))))
    print("Using Solution4:",tuple(t))


shop1 =(10, 4, 5)
shop2 =(2, 5, 18)
print(" Shop1 Tuple:",shop1)
print(" Shop2 Tuple:",shop2)

maxElementIntuple1(shop1,shop2)
maxElementIntuple2(shop1,shop2)
maxElementIntuple3(shop1,shop2)
maxElementIntuple4(shop1,shop2)



