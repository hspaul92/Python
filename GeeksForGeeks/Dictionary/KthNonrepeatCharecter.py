from collections import OrderedDict 

def kthNonRepeatingCharecter(string,k):
    dic = OrderedDict.fromkeys(string,0)
    for charecter in string:
        dic[charecter]= dic[charecter]+1
    #Find Non-Repeated Charecter
    nonRepeateCharecter =[k for k,v in dic.items() if v ==1]
    #Find K'th Non-Repeated Charecter
    if len(nonRepeateCharecter) < k: 
       return 'K value is higher than no of non-repeating charecters' 
    else:
       return nonRepeateCharecter[k-1]


input = "geeksforgeeks"
print('TheOriginal String:',input)
print('First Non Repeating Charecter :',
       kthNonRepeatingCharecter(input, 1))
print('Second Non Repeating Charecter :',
       kthNonRepeatingCharecter(input, 2))
print('Third Non Repeating Charecter :',
       kthNonRepeatingCharecter(input, 3))
