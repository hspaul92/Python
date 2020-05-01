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

     print("Converted List1 :",l1)
     print("Converted List2 :",l2)

     result_tuple =tuple(zip(l1,l2))
     print("Zipped result :",result_tuple)


input1 = (2001,2002,2003,2004,2005,2006)
input2 = ('AWS','GOOGLE','APPLE')
zipUnevenTuple1(input1,input2)
zipUnevenTuple1(input2,input1)

