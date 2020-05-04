#######
#dic = {'Manjeet' : 1, 'Akash' : '2', 'Akshat' : '3', 'Nikhil' : 1}
#dic = {'Akshay':'Kumar','Anil':'Kapur','Ranbir':'Kapur','Sunil':'Setti'}
#dic = {'Akshay':'Kumar','Anil':'Kapur','Ranbir':'Singh','Sunil':'Setti'}


def duplicateValues(d):
    lis=[]
    dic={}
    for key  in d:
        if d[key] in lis:
           dic[key]=d[key]          
        else:
           lis.append(d[key])          

    if len(dic) ==0:
       print('There are no keys with Duplicate values')
    else:
       print(dic)                          
           
dic1 = {'Akshay':'Kumar','Anil':'Kapur','Ranbir':'Kapur','Arjun':'Kapur'}
duplicateValues(dic1)
dic2 = {'Akshay':'Kumar','Anil':'Kapur','Ranbir':'Singh','Sunil':'Setti'}
duplicateValues(dic2)   




