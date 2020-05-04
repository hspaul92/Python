# Question: Convert a tuple to a string
# Input : ('a', 'b', 'c', 'd', 'e')
# Output : abcde

# Input : ('g', 'e', 'e', 'k', 's')
# Output : geeks


# Solution:1 Using tuple comprehension and string + operator
def convertTupleToString1(t):
    string1 = ''
    for x in t:
        string1 +=x
    print("Solution1: ",string1 )


# Solution:2 Using string join() function
def convertTupleToString2(t):
    string2 = ''.join(t)
    print("Solution2: ", string2)


# Solution:3 Using reduce function
from  functools import reduce
def convertTupleToString3(t):
    string3 = reduce(lambda x,y:x+y,  t )
    print("Solution3: ", string3)

input_tuple =  ('a', 'b', 'c', 'd', 'e')
print("Input Tuple :",input_tuple)
convertTupleToString1(input_tuple)
convertTupleToString2(input_tuple)
convertTupleToString3(input_tuple)