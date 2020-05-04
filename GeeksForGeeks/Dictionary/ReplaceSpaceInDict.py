#Solution:1 Using translate
def replaceSpaceInDict1(a):
    t = {x.translate({32:None}):y for x,y in a.items()}                                
    print(t)

dic= {'10 0':'Google','2   02':'Apple','   300   ':'Amazon','400':'MS'}
print("original Keys:",dic)
replaceSpaceInDict1(dic)

#Solution:2 Using replace
def replaceSpaceInDict1(a):
    t = {x.replace(' ',''):y for x,y in a.items() }
    print(t)

dic2= {'10 0':'Google','2   02':'Apple','   300   ':'Amazon','400':'MS'}
print("original Keys:",dic2)
replaceSpaceInDict1(dic2)    
