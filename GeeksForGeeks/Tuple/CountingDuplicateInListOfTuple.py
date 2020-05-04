# Question: Counting Duplicate Element in list OF Tuple
# Input : [('a', 'e'), ('b', 'x'), ('b', 'x'), ('a', 'e'), ('b', 'x'')]
# Output :('a', 'e') – 2   ('b', 'x') – 3


# Solution:1 Using dict() and list comprehension
def countingDuplicateInListOfTuple1(l):
    s = dict()
    for x in l :
        s[x] = s.get(x,0)+1
    print("Duplicate Elements :", [(x,y)  for x,y in s.items() if y>1])


# Solution:2 Using dict() and list comprehension
from collections import Counter
def countingDuplicateInListOfTuple2(l):
    t = Counter(l)
    print("Duplicate Elements :", [(x,y)  for x,y in t.items() if y>1])


input_list1 =  [('a', 'e'), ('b', 'x'), ('b', 'x'), ('a', 'e'), ('b', 'x')]
print("Input List :",input_list1)
countingDuplicateInListOfTuple1(input_list1)
countingDuplicateInListOfTuple2(input_list1)