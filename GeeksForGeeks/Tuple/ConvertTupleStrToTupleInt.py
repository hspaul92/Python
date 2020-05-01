# Solution:1  Converting String to Tuple
def convertTupleStrToTupleInt1(s):
    l = tuple(s)
    print("After Direct Conversion : ", l)
    print("Type  :", type(l))
# Note : Here when we convert string into tuple it will convert each element in string
# including '(' and ')' i.e open and close bracket as tuple elements .
# So output of tuple(s) will be('(', '1', ',', '2', ',', '3', ',', '4', ')') .
# But we need only integer element . So We have to remove those in string itself
# using replace method as below
    cleaned_str= s.replace('(','').replace(')','')
    gen = (int(x) for x in cleaned_str.split(','))  #It will cretae generater object
    print("Type   : ", type(gen))
    tup = tuple(gen)
    print("Output : ",tup)
    print("Type   : ",type(tup))

# Taking input as Tuple using eval()
def convertTupleStrToTupleInt2():
    user_input = eval(input('Enter Tuple of Integer :'))
    print("User Input :",user_input)
    print("User Input type :",type(user_input))

# Driver programme
input_tuple_string = '(1,2,3,4)'
print("Input : ",input_tuple_string)
print("Type  :",type(input_tuple_string))

# Using Solution 1:
convertTupleStrToTupleInt1(input_tuple_string)

# Using Solution 2:
convertTupleStrToTupleInt2()
