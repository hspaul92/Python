# Create list of tuples from given list having number and its cube as tuple elements
# Example:
# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]

# Solution1: Using list comprehension and multipication
def createTupleFromlist1(l):
    t1 = [(x, x*x*x) for x in l]
    print("Solution1: ",t1)

# Solution2: Using list comprehension and power() function
def createTupleFromlist2(l):
    t2 = [(x, pow(x,3)) for x in l]
    print("Solution2: ",t2)

# Solution2: Using iteration and append() method of list
def createTupleFromlist3(l):
    t3 = []
    for x in l:
        t3.append((x,x*x*x))
    print("Solution3: ", t3)


lis = [1, 2, 3]
print("Input List :",lis)
createTupleFromlist1(lis)
createTupleFromlist2(lis)
createTupleFromlist3(lis)