# Write a Python programme to Merge two lists into list of tuples
#
# Scenario 1
# Input : list1 = [1, 2, 3],  list2 = ['a', 'b', 'c']
# Output : [(1, 'a'), (2, 'b'), (3, 'c')]

# Scenario :2 If coresponding element is not available then reject that element from output
# Input : list1 = [1, 2, 3, 4]  , list2 = [ 1, 4, 9]
# Output : [(1, 1), (2, 4), (3, 9)]

# Solution:1 Using list slicing and zip() method
def merge2ListIntoListOfTuple1(l1,l2) :
    print("l1 :",l1, "  l2 :",l2)
    if len(l1) > len(l2):
        l1 =  l1[0:len(l2)]
    elif len(l1) < len(l2):
        l2 = l2[0:len(l1) ]
    output_list =  list(zip(l1,l2))
    print("Solution1 : Output ",output_list)

# Solution:2 Using
def merge2ListIntoListOfTuple2(l1, l2):
    print("l1",l1)
    print("l2",l2)
    indexd_list1= []
    indexd_list2= []
    for x in l1:
        indexd_list1.append(x:l1.index(x))

    print(indexd_list1)




    #indx_tuple1 = list(l1.index(x): x for x in l1)
    #indx_tuple2 = list(l2.index(y): y for y in l2)
    #print(indx_tuple1)
    #print(indx_tuple2)
    #utput_list = []
    #for i in range(0, len(indx_tuple1)):
    #        if indx_tuple1[i][1]== indx_tuple2[i][1]:
     #           output_list.append((indx_tuple1[0],indx_tuple1[0]))
    #print("Solution2 : Output ", output_list)




# Solution:3 Using list slicing and zip() method
def merge2ListIntoListOfTuple3(l1,l2) :
    print("l1 :",l1, "  l2 :",l2)
    output_list = [(l1_ele,l2_ele)
                   for l1_indx,l1_ele in enumerate(l1)
                   for l2_indx,l2_ele in enumerate(l2)
                   if l1_indx == l2_indx
                   ]
    print("Solution3 : Output ",output_list)




list1 = [1, 2, 3, 4]
list2 = [ 1, 4, 9]
merge2ListIntoListOfTuple1(list1,list2)

list3 = [1, 2, 7, 4]
list4 = [ 1, 4, 9]
merge2ListIntoListOfTuple2(list3,list4)

list5 = [1, 2, 3]
list6 = [ 1, 4, 0, 3]
merge2ListIntoListOfTuple3(list5,list6)

