# Write a programme to sum tuples having same first values
# Input: [(1, 13), (2, 190), (3, 82), (1, 12)]
# Output: [(1, 25), (2, 190), (3, 82)]

# Input: [(1, 13), (1, 190), (3, 25), (1, 12)]
# Output: [(1, 215), (3, 25)]


# Solution1 : Using dict
def SumOfTupleHavingSameFirstValue(l):
    d = dict()
    for x in l :
        if x[0] in d:
           d[x[0]] = d[x[0]]+x[1]
        else :
            d[x[0]]= x[1]
    output_list =  [ (x,y) for x,y in d.items()]
    print("Final Output :",output_list)

# Solution :2
def SumOfTupleHavingSameFirstValue(l):
    


input_list= [(1, 13), (2, 190), (3, 82), (1, 12)]
print("Input List :",input_list)
SumOfTupleHavingSameFirstValue(input_list)




