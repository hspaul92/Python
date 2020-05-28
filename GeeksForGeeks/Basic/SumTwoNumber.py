# Write a Python program to add two numbers
# Scenario:1
# Input: num1 = 5, num2 = 3
# Output: 8

# Scenario:2
# Input: num1 = 13, num2 = 6
# Output: 19


#Solution :1
def addTwoNumber(a,b):
    return a+b


inp1 = int(input("Enter First Number:"))
inp2 = int(input("Enter Second Number:"))
print("Sum Of Two Numbers:",addTwoNumber(inp1,inp2))