def findPositiveVale(d):
    result = dict(filter(lambda x: x[1] >= 0, d.items()))
    print(result)            

d1={'a': 1, 'c': -3, 'd': 7, 'b': -2, 'e': 0}
findPositiveVale(d1)

