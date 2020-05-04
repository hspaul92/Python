import collections


def sumOfvalues(l):
    result = {}
    for d in l:
        for k in d.keys():
            result[k] = result.get(k, 0) + d[k]
    print(result)


dict = [{'a': 5, 'b': 10, 'c': 90}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}]
sumOfvalues(dict)


counter = collections.Counter()
for d in dict:
    counter.update(d)

# result = dict(counter)
print(str(counter))

