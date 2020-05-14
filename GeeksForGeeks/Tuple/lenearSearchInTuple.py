def lenearSearch(l,e):
    if e in l:
        print(e, " is present at ", l.index(e) ," index")
    else :
        print(e ," is not present in list ")


input_list = eval(input ("Enter a list of items:"))
print("Entered list :",input_list)
search_element = eval(input("Enter the Element You Want to Search:"))
print("Search Element :",search_element)
lenearSearch(input_list,search_element)
