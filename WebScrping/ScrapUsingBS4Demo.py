import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

r = requests.get(url)
pageContent = r.content

#print(pageContent)
#print(type(pageContent))

soup = BeautifulSoup(pageContent,'html.parser')
#print(soup.prettify())
#print(soup.title.string)
#print(soup.find_all('title'))

#print(soup.find('p'))
#print("* 0 *",soup.find_all('p')[0])
# print("* 1 *",soup.find_all('p')[1])
# print("* 2 *",soup.find_all('p')[2])
# print("* 3 *",soup.find_all('p')[3])
# print("* 4 *",soup.find_all('p')[4])

# Find Anchor
#print(soup.find('a')['class'])

#print(soup.find('p'))
#rint(soup.find('p')['class'])
#print(soup.find('p').get('class'))
#print(soup.find_all("p"))
#for x  in (soup.find_all("p")):
#    print(x.get('class'))
#    print(x.get_text())

#print(soup.find_all("button"))

#print(soup.find_all("div"))

#print("Class : ",soup.find("div")['class'])
#print("ID : ",soup.find("div")['id'])
#print(soup.find("div"))


# print(soup.find("button")['aria-controls'])
# print("Button aria-expanded",soup.find("button")['aria-expanded'])
# print("Button aria-label ",soup.find("button")['aria-label'])
# print("Button aria class",soup.find("button")['class'])
# print("Button target",soup.find("button")['data-target'])
# print("Button toggle",soup.find("button")['data-toggle'])
# print("Button type",soup.find("button")['type'])
# print(soup.find("button"))









#for x in soup.find_all('a'):
#   print( x)





