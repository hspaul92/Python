# Write a python programme to  find the max values in list of Tuple
# Original list : [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]
# The name with maximum score is : Manjeet

# Solution:1 Using max() with lambda expression
def MaximumValueInListOfTuple1(x):
    top_value = max(x,key= lambda x:x[1])
    print("Solution1: Maximum mark ",top_value)

# Solution:2 Using max() with itemgetter()
from  operator import itemgetter

def MaximumValueInListOfTuple2(x):
    top_value = max(x, key= itemgetter(1))
    print("Solution2: Maximum mark ",top_value)




input_list = [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]
print ("Input Marks :",input_list)
MaximumValueInListOfTuple1(input_list)
MaximumValueInListOfTuple2(input_list)
