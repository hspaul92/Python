from collections import Counter 

#Solution:1
def checkTwoHalves(input):
    length = len(input)
    # Break input string in two parts
    if (length % 2 != 0):
       first = input[0:int(length / 2)] 
       second = input[int(length / 2) + 1:] 
    else: 
        first = input[0 : int(length/2)] 
        second = input[int(length/2) :] 

	# Convert both halves into dictionary and compare 
    if Counter(first) == Counter(second): 
       print ('YES')
    else: 
      print ('NO')

word1= 'abbaab'
print("Original Word:",word1)
checkTwoHalves(word1)

word2='abccab'
print("Original Word:",word2)
checkTwoHalves(word2)

