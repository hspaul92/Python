#Question:
# Remove all strings from a list of tuples
# Input : [(1, 'Paras'), (2, 'Jain'), (3, 'GFG'), (4, 'Cyware')]
# Output :   [(1), (2), (3), (4)]
# Input : [('string', 'Geeks'), (2, 225), (3, '111')]
# Output : [(), (2, 225), (3,)]

# Solution:1  Using nested for in  list comprehension
def removeStringFromTupleOfList1(l):
    l = [tuple( y for y in x if not isinstance(y,str)) for x in l]
    print("Solution 1:",l)

# Solution:2  Using filter with lambda function in  list comprehension
def removeStringFromTupleOfList2(l):
    l = [tuple(filter(lambda x: not isinstance(x,str) ,x )) for x in l]
    print("Solution 1:",l)

def removeStringFromTupleOfList2(l):
    l = [tuple(filter(lambda x: not isinstance(x,str) ,x )) for x in l]
    print("Solution 1:",l)

lis = [(1, 'Paras'), (2, 'Jain'), ('GFG', 3), (4, 'Cyware')]
print("Input :",lis)
removeStringFromTupleOfList1(lis)
removeStringFromTupleOfList2(lis)
