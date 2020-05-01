# Case:1 If Corresponding element is available then zip it ,
#             If not, then Zip with Null
# Example:
# First Input  : (2001, 2002, 2003, 2004, 2005, 2006)
# Second Input : ('AWS', 'GOOGLE', 'APPLE')
# FirstZipSecond :((2001, 'AWS'), (2002, 'GOOGLE'), (2003, 'APPLE'), (2004, 'None'), (2005, 'None'), (2006, 'None'))
# SecondZipFirst :(('AWS', 2001), ('GOOGLE', 2002), ('APPLE', 2003), ('None', 2004), ('None', 2005), ('None', 2006))

# **************************************************************
# Case:2 If Corresponding element is available then zip it ,
#             If not, use cyclic zip

# First Input  : (2001, 2002, 2003, 2004, 2005, 2006)
# Second Input : ('AWS', 'GOOGLE', 'APPLE')
# Input1 Zip Input2 : [(2001, 'AWS'), (2002, 'GOOGLE'), (2003, 'APPLE'), (2004, 'AWS'), (2005, 'GOOGLE'), (2006, 'APPLE')]
# Input2 Zip Input1 : [('AWS', 2001), ('GOOGLE', 2002), ('APPLE', 2003), ('AWS', 2004), ('GOOGLE', 2005), ('APPLE', 2006)]


# *************************************************************
# For Case:1
# Solution:1 Using list() and append()
def  zipUnevenTuple1(t1,t2):
     print("First Input  :", t1)
     print("Second Input :", t2)
     l1= list(t1)
     l2= list(t2)
     if len(l1) > len(l2):
        for i in range (0,int(len(t1)-len(t2))):
            l2.append('None')
     elif len(l2) > len(l1):
        for i in range(0, int(len(t2) - len(t1))):
            l1.append('None')

     #print("Converted List1 :",l1)
     #print("Converted List2 :",l2)

     result_tuple =tuple(zip(l1,l2))
     return result_tuple


input1 = (2001,2002,2003,2004,2005,2006)
input2 = ('AWS','GOOGLE','APPLE')
print("***** Case1: Generic Zip *****")
result1= zipUnevenTuple1(input1,input2)
print("Input2 Zip Input1:",result1 ,"\n")

result2= zipUnevenTuple1(input2,input1)
print("Input1 Zip Input2:",result2,"\n\n")





# For Case 2:

# Solution:1 Using inbuilt enumerate() function
def zipUnevenTuple2(t1,t2):
    print("First Input  :", t1)
    print("Second Input :", t2)
    l1=list(t1)
    l2=list(t2)
    zipped_list = []
    if len(l1) > len(l2):
       for i,j in enumerate(l1):
           zipped_list.append((j,l2[i%len(l2)] ))
    else:
        for x,y in enumerate(l2):
            zipped_list.append((l1[x%len(l1)],y))
    return zipped_list


# Solution:2 Using inbuilt index() function

def zipUnevenTuple3(t1,t2):
    print("First Input  :", t1)
    print("Second Input :", t2)
    l1=list(t1)
    l2=list(t2)
    zipped_list = []
    if len(l1) > len(l2):
       for x in l1:
           zipped_list.append((x,l2[l1.index(x)%len(l2)] ))
    else:
       for y in l2:
           zipped_list.append((l1[l2.index(y)%len(l1)],y))
    return zipped_list


# Solution:3 Using inbuilt cycle function
from itertools import cycle

def zipUnevenTuple4(t1,t2):
    print("First Input  :", t1)
    print("Second Input :", t2)
    result = list(zip(t1, cycle(t2))
          if len(t1) > len(t2)
           else
               zip(cycle(t1), t2))
    return result


input1 = (2001,2002,2003,2004,2005,2006)
input2 = ('AWS','GOOGLE','APPLE')
print("***** Case2: Cyclic Zip *****")


print("***** Using Solution 1: enumerate() function ")
print("Input1 Zip Input2 :", zipUnevenTuple2(input1,input2),"\n")
print("Input2 Zip Input1 :", zipUnevenTuple2(input2,input1),"\n\n")


print("***** Using Solution 2: index() function")
print("Input1 Zip Input2 :", zipUnevenTuple3(input1,input2),"\n")
print("Input2 Zip Input1 :", zipUnevenTuple3(input2,input1),"\n\n")

print("***** Using Solution 3: cycle() function" )
print("Input1 Zip Input2 :", zipUnevenTuple4(input1,input2),"\n")
print("Input2 Zip Input1 :", zipUnevenTuple4(input2,input1),"\n\n")


