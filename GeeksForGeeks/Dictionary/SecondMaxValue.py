#Solution:1 Using inbuilt sorted() function 
def secondMaxValue(d):
    print(list(sorted(d.values()))[-2])


dic ={'Sony':2001,'Apple':2003,'Amazon':2002,'Google':2004}
secondMaxValue(dic)
