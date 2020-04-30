# Solution:1 Using List Comprehension
def convertListOfTupleToDict1(l):
    d1 = {x[0]: x[1] for x in l}
    print("Result Dictionary", d1)

# Solution:2 Using List Comprehension  and dict key assignment method
def convertListOfTupleToDict2(l):
    d2={}
    for x in l:
        d2[x[0]]=x[1]
    print("Result Dictionary", d2)



# Driver programme
lis = [(2001, 'Amazon'), (2002, 'Google'), (2003, 'Apple')]
print("Original list of tuple:", lis)

# Using Solution
convertListOfTupleToDict1(lis)
convertListOfTupleToDict2(lis)


