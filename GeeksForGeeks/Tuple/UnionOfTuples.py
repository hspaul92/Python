# Input Tuple 1 : (3, 4, 5, 6)
# Input tuple 2 : (5, 7, 4, 10)
# Union Of tuples: (3, 4, 5, 6, 7, 10)


#Solution1: Using set() and union()
def unionOfTuples1(t1,t2):
    t2 =set(t1).union(set(t2))
    print("Using Solution1 :", tuple((t2)),"\n")

def unionOfTuples2(t1,t2):
    t1ADDt2 =  t1+t2
    result = tuple(set(t1ADDt2))
    print("Using Solution2 : ", result)


input_tuple1 = (3,4,5,6)
input_tuple2 = (5,7,4,10)
print("Input Tuple1:",input_tuple1)
print("Input Tuple2:",input_tuple2)


#Using Solution :1
unionOfTuples1(input_tuple1,input_tuple2)

#Using Solution :2
unionOfTuples2(input_tuple1,input_tuple2)

