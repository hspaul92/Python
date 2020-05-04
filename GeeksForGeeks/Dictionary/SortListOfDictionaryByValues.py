#Solution:1  Using inbuilt sorted() and itemgetter() method
from operator import itemgetter
def sortListOfDictionaryByValues1(l):
    salary_sorted_asc = sorted(l,key=itemgetter('Salary'))
    print(salary_sorted_asc)
    salary_sorted_desc = sorted(l,key=itemgetter('Salary'),reverse=True)
    print(salary_sorted_desc)

#Solution:2  Using inbuilt sorted() and lambda() method
def sortListOfDictionaryByValues2(l):
    salary_sorted_asc = sorted(l,key=itemgetter('Salary'))
    print(salary_sorted_asc)
    salary_sorted_desc = sorted(l,key= lambda x:x['Salary'] ,reverse=True)
    print(salary_sorted_desc)

#Solution:3  Using longway
def sortListOfDictionaryByValues3(l):
    flat_list = [(x['fname'],x['Age'],x['Salary']) for x in l]
    print(flat_list)
    salary_sorted_asc = sorted(flat_list, key= lambda x: x[2])
    print(salary_sorted_asc)
    salary_sorted_desc = sorted(flat_list,key= lambda x: x[2] ,reverse=True)
    print(salary_sorted_desc)


lis=[{'fname':'IronMan','Age':100,'Salary':500000},
     {'fname':'Superman','Age':103,'Salary':100000},
     {'fname':'WonderWoman','Age':107,'Salary':300000},
     {'fname':'SpiderMan','Age':90,'Salary':400000},
     {'fname':'Shaktiman','Age':89,'Salary':300000},
     {'fname':'Aquaman','Age':120,'Salary':350000}]

sortListOfDictionaryByValues1(lis)
sortListOfDictionaryByValues2(lis)
sortListOfDictionaryByValues3(lis)

