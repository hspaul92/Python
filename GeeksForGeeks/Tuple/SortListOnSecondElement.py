# Question: Sorting list of tuple based on second element
# Scenario:1
# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)]
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
# Scenario:2
# Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
# Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]

# Solution:1 Using sorted() with lambda function
def sortListOnSecondElement1 (l):
    sl1 = sorted (l , key= lambda x:x[1])
    print("Using Solution1: Asc Sorted :",sl1)
    rsl1 = sorted (l , key= lambda x:x[1], reverse=True)
    print("Using Solution1:Desc Sorted :",rsl1)


# Solution:2 Using sorted() with itemgetter() function
from operator import itemgetter
def sortListOnSecondElement2 (l):
    sl2 = sorted (l , key= itemgetter(1))
    print("Using Solution2: Asc Sorted :",sl2)
    rsl2 = sorted (l , key= itemgetter(1), reverse=True)
    print("Using Solution2:Desc Sorted :",rsl2)


# Solution:3 Using sorted() with lambda function
def sortListOnSecondElement3(l):
    l.sort(key=lambda x: x[1])
    print("Using Solution3: Asc Sorted :",l)
    l.sort(key=lambda x: x[1], reverse=True)
    print("Using Solution3:Desc Sorted :",l)

# Solution:4 Using sorted() with itemgetter() function
def sortListOnSecondElement4(l):
    from operator import itemgetter
    l.sort(key=itemgetter(1))
    print("Using Solution4: Asc Sorted :",l)
    l.sort(key= itemgetter(1), reverse=True)
    print("Using Solution4:Desc Sorted :",l)





input_list1= [('for', 24), ('Geeks', 8), ('Geeks', 30)]
print("Input : ",input_list1)
sortListOnSecondElement1(input_list1)
sortListOnSecondElement2(input_list1)
sortListOnSecondElement3(input_list1)
sortListOnSecondElement4(input_list1)


input_list2 =[('452', 10), ('256', 5), ('100', 20), ('135', 15)]
print("Input : ",input_list2)
sortListOnSecondElement1(input_list2)
sortListOnSecondElement2(input_list2)
sortListOnSecondElement3(input_list2)
sortListOnSecondElement4(input_list2)


