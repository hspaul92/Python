#Solution1: Using Comprehesion and isinstance() function
def countLengthOfKey(p):
    length_of_each_list_value = [len(d[x]) for x in d if isinstance(d[x], list)]
    sum_of_length= sum(length_of_each_list_value)
    print(sum_of_length)            


d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9], 
     'B' : 34, 
     'C' : 12, 
     'D' : [7, 8, 9, 6, 4] }
print("Original Dictionary:",d)
countLengthOfKey(d)

