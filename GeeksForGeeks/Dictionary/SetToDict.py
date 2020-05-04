#Solution:1
def setToDict(s):
    d = dict.fromkeys(s,0)
    print("Dictionary  :",d)

st =(2001,2002,2003,2004)
print("Original Set:",st)
setToDict(st)



#Solution:2
def setToDict2(s):
    d= {x:0 for x in s}
    print("Dictionary  :",d)

st =(2001,2002,2003,2004)
print("Original Set:",st)
setToDict2(st)


#Solution:3 Using iteration
def setToDict3(s):
    d={}
    for e in s:
        d[e]=0
    print("Dictionary  :",d)
st =(2001,2002,2003,2004)

print("Original Set:",st)
setToDict3(st)


#Solution:4 Using inbuilt zip() method and list replicate operater
def setToDict4(s):
    t= zip(list(s),[0]*len(s))
    d =dict(t)
    print("Dictionary  :",d)

print("Original Set:",st)
setToDict4(st)


#Solution:5 
