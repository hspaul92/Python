# Solution:1 Using List Comprehension
def convertListOfTupleToDict(l):
    d={x[0]:x[1] for x in l}
    print("Result Dictionary",d)

lis= [(2001,'Amazon'),(2002,'Google'),(2003,'Apple')]
print("Original list of tuple:",lis)
convertListOfTupleToDict(lis)