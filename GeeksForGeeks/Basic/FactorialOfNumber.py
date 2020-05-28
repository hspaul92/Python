# Write a Python Program to find  factorial of a number
# Explanation : Factorial of 0 is 1 , for any other number .. n * (n-1) * (n-2) * (n-3) ..... 1
# Scenario1 : Input:6  >> Output:720
# Scenario2 : Input:0  >> Output:1

# Solution:1 Using Iteration with decreasing value
def factOfNumber1(n):
    mul= 1
    if n != 0:
        while (n!=0):
            mul = mul*n
            n=n-1
        return mul
    else:
        return 1


# Solution:2 Using Iteration with increasing value
def factOfNumber2(n):
    mul =1
    startvalue=1
    if n!= 0:
        while (startvalue<=n):
            mul =mul *startvalue
            startvalue=startvalue+1
        return mul
    else:
        return 1

# Solution:3 Using recursion
def factOfNumber3(n):
    if n == 0:
       return 1
    else:
       return n*factOfNumber3(n-1)


# Driver Code
number = int(input("Enter A Non Negative Number:"))
print("Using Solution1: Factorial of {} is {}".format(number, factOfNumber1(number)))
print("Using Solution2: Factorial of {} is {}".format(number, factOfNumber2(number)))
print("Using Solution3: Factorial of {} is {}".format(number, factOfNumber3(number)))

