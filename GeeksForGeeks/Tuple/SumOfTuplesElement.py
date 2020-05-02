# The original tuple is : (7, 8, 9, 1, 10, 7)
# Sum Of Elemnets: 42

# Solution:1 Using tuple Comprehension
def SumOfTuplesElement(t):
    sum=0
    for x in t:
        if isinstance(x,int)== True :
           sum += x
        else:
            print(" Input Tuple Contains Non Integer Element :", x )
            break
    if sum!=0:
       print("Sum Of Element :",int(sum))
    else:
        print("Programme break in between due to non int element")


# Solution: Using inbuilt sum() method
def SumOfTuplesElement2(t):
    sumOfList = sum(t)
    print("Sum:",sumOfList)


input_tup1 = (7, 8, 9, 1, 10, 7)
input_tup2 = (7, 8, 9, 1, '10', 7)
print("Input :",input_tup1)

#Using Solutuon1
SumOfTuplesElement(input_tup1)
SumOfTuplesElement(input_tup2)

#Using Solutuon2
SumOfTuplesElement2(input_tup1)


