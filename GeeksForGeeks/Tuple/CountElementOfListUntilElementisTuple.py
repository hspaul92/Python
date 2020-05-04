# Scenario
# --------
# Input : [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
# Output : 4
# Input : [4, (5, 6), 10, (1, 2, 3), 11, 2, 4]
# Output : 1

# Solution:1 Using isinstance()

def countElementOfList(l):
    count =0
    for x in l:
        if isinstance(x,tuple) == True:
           break
        else:
            count+=1
    print("No of Element Until First Tuple :",count)


input_list1 = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
print("Input :",input_list1)
countElementOfList(input_list1)

#Output : 4

input_list2 = [4, (5, 6), 10, (1, 2, 3), 11, 2, 4]
print("Input :",input_list2)
countElementOfList(input_list2)


#Output : 1
