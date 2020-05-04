#Solution:1 Using comprehesion and sorted() method
def topThreeValuesAndThereKeys1(d):
    top_three_values = list(sorted(d.values()))[-3:]
    result = {x:y for x,y in d.items() if y in top_three_values }
    print(result)

dic1 = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}
print("Original Dictionary:",dic1)
topThreeValuesAndThereKeys1(dic1)


#Solution:2 Using counter() method
from collections import Counter
def topThreeValuesAndThereKeys2(d):
    count = Counter(d)
    result = count.most_common(3)
    print(dict(result))

dic2 = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}
print("Original Dictionary:",dic2)
topThreeValuesAndThereKeys2(dic2)
    

#Solution:3 Using nlargest()
from heapq import nlargest 
def topThreeValuesAndThereKeys3(d):
    top_three_values = dict(nlargest(3,d.items(), key =  lambda x:x[1]))
    print(top_three_values)
    
dic3 = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}
print("Original Dictionary:",dic3)
topThreeValuesAndThereKeys3(dic3)

