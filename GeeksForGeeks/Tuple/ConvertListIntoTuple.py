# Write a programme to convert list into tuple
#
# Scenario :1
# Input : [1, 2, 3, 4]
# Output : (1, 2, 3, 4)
#
# Scenario :2
# Input : ['a', 'b', 'c']
# Output : ('a', 'b', 'c')

# Solution:1 Using inbuilt tuple() function
def convertListIntoTuple1(l) :
    return tuple(l)


# Solution:2    Using List comprehension
def convertListIntoTuple2(l):
    return tuple(x for x in l)


input_list = [1, 2, 3, 4]
print("Input List :",input_list)
print("Using Solution1: After Converting list into tuple :",convertListIntoTuple1(input_list) )
print("Using Solution2: After Converting list into tuple :",convertListIntoTuple2(input_list) )

