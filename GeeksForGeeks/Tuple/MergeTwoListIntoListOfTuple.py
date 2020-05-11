# Write a Python programme to Merge two lists into list of tuples
#
# Scenario 1
# Input : list1 = [1, 2, 3],  list2 = ['a', 'b', 'c']
# Output : [(1, 'a'), (2, 'b'), (3, 'c')]

# Scenario :2
# Input : list1 = [1, 2, 3, 4]  , list2 = [ 1, 4, 9]
# Output : [(1, 1), (2, 4), (3, 9), (4, '')]

# Solution:1 Using append() and zip() method
def MergeTwoListIntoListOfTuple1(l1,l2):
    print("Input List l1 :",l1)
    print("Inout List l2 :",l2)
    if len(l1) > len(l2):
        l2.append( (len(l1)-len(l2)) * '' )
    elif len(l1) < len(l2) :
        l1.append( (len(l2)-len(l1)) * '' )

    output_list =  list(zip(l1,l2))
    print("Solution1 : Output ",output_list)


# Solution:2 Using append() and list comprehension method
def MergeTwoListIntoListOfTuple2(l1,l2):
    print("Input List l1 :",l1)
    print("Inout List l2 :",l2)
    if len(l1) > len(l2):
        l2.append( (len(l1)-len(l2)) * '')
    elif len(l1) < len(l2):
        l1.append( (len(l2)-len(l1)) * '')

    print ("L1:",l1 ,"L2 :",l2 )
    output_list = [(l1[i],l2[i]) for i in range (0,len(l1))]
    print("Solution2 : Output ",output_list)


# Solution:3 Using append(), map() and lambda function
def MergeTwoListIntoListOfTuple3(l1,l2):
      print("Input List l1 :",l1)
      print("Input List l2 :",l2)
      if len(l1) > len(l2):
        l2.append( (len(l1)-len(l2)) * '')
      elif len(l1) < len(l2):
        l1.append( (len(l2)-len(l1)) * '')
      output_list = list(map(lambda x, y:(x,y), l1, l2))
      print("Solution3 : Output ",output_list)


# Solution:4 Using append(), iteration
def MergeTwoListIntoListOfTuple4(l1,l2):
    print("Input List l1 :",l1)
    print("Input List l2 :",l2)
    if len(l1) > len(l2):
        l2.append( (len(l1)-len(l2)) * '')
    elif len(l1) < len(l2):
        l1.append( (len(l2)-len(l1)) * '')
    output_list = []

    for i in range(0,len(l1)) :
        t = (l1[i],l2[i])
        output_list.append(t)
    print("Solution4 : Output ", output_list)


input_list1 =  [1, 2, 3, 4]
input_list2 =  [ 1, 4, 9]
MergeTwoListIntoListOfTuple1(input_list1,input_list2)
input_list3 =  [1, 2, 3]
input_list4 =  [ 1, 4, 8, 9]
MergeTwoListIntoListOfTuple2(input_list3,input_list4)
input_list5 =  [1, 2, 3]
input_list6 =  [ 1, 4, 8, 9]
MergeTwoListIntoListOfTuple3(input_list5,input_list6)
input_list7 =  [1, 2, 3]
input_list8 =  [ 1, 4, 8, 9]
MergeTwoListIntoListOfTuple4(input_list7,input_list8)