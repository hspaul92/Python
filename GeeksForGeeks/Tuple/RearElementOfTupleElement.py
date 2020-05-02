# Solution1: Using List comprehension with slicing technique
def rearElement1(t):
    l1 = [x[-1] for x in t ]
    print("Using Solution1 : List Of rear elements of tuple :",l1)

# Solution2: Using length  comprehension with inbuilt length function
def rearElement2(t):
    l2 = [x[len(x)-1] for x in t ]
    print("Using Solution2 : List Of rear elements of tuple :",l2)

# Solution3: Using  for loop with inbuilt length function and list append() function
def rearElement3(t):
    l3 = []
    for x in t :
        indx = len(x)-1
        l3.append(x[indx])
    print("Using Solution3 : List Of rear elements of tuple :",l3)



inputStr=  ('AWS','Google','Sony','Apple')
print("Input Tuple :",inputStr)
rearElement1(inputStr)
rearElement2(inputStr)
rearElement3(inputStr)