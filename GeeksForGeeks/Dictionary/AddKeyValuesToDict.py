# Solution:1 Using dictionary subscript
def addKeyValuesToDict1(d):
    key = eval(input("Enter New Key:"))
    value = eval(input("Enter New Value:"))
    d[key] = value
    print("After Adding New Element:", d)


dic = {2001: 'Apple', 2002: 'Amazon', 2003: 'Google'}
print("Original Dictionary:", dic)
addKeyValuesToDict1(dic)


# Solution:2 Using update method
def addKeyValuesToDict2(d):
    key = eval(input("Enter New Key:"))
    value = eval(input("Enter New Value:"))
    d.update({key: value})
    print("After Adding New Element:", d)


dic = {2001: 'Apple', 2002: 'Amazon', 2003: 'Google'}
print("Original Dictionary:", dic)
addKeyValuesToDict2(dic)


# Solution:3 Using * operater
def addKeyValuesToDict3(d):
    key = eval(input("Enter New Key:"))
    value = eval(input("Enter New Value:"))
    d.update({key: value})
    new_dict = {**d, **{key: value}}
    print("After Adding New Element:", new_dict)


dic = {2001: 'Apple', 2002: 'Amazon', 2003: 'Google'}
print("Original Dictionary:", dic)
addKeyValuesToDict2(dic)


# Solution:4 Using __setitem__  method
def addKeyValuesToDict3(d):
    key = eval(input("Enter New Key:"))
    value = eval(input("Enter New Value:"))
    d.__setitem__(key, value)
    new_dict = {**d, **{key: value}}
    print("After Adding New Element:", new_dict)



