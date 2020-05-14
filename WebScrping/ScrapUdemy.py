import requests
from bs4 import BeautifulSoup
import csv
# url = "https://www.amazon.in/s/ref=s9_acsd_hps_bw_c2_x_c2cl?node=4348234031&rw_html_to_wsrp=1&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-8&pf_rd_r=YQAE8DYXF5MBY019MWD7&pf_rd_t=101&pf_rd_p=fb404602-5b0a-4598-80e7-84de23fd8d64&pf_rd_i=10591963031"
# header = { 'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
# r = requests.get(url,headers=header)
# pageContent = r.content
#
# soup = BeautifulSoup(pageContent,'html.parser')
# #print(soup.prettify())
# for x in soup.find_all('h2') :
#     print(x.get_text())
# #div class="udlite-heading-sm udlite-focus-visible-target
# #<h2 data-attribute="The Alchemist" data-max-rows="0" class="a-size-medium s-inline s-access-title a-text-normal">The Alchemist</h2>

csv_file =open('scrap_data_CoreySchafer_Page3.csv','w',newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['HeadLine','Published On','Author','Content','YouTube','Category','Tags'])

source = requests.get('https://coreyms.com/').text
soup   =  BeautifulSoup(source,'lxml')
#print(soup.prettify())

for article in soup.find_all('article'):
    #print(article.prettify())
    print("***** **** *****")

    headline = article.h2.a.text
    print(headline)

    published_on  = article.find('time',class_ ='entry-time').get_text()
    print("Article Published On :", published_on)

    author = article.find('span',class_ ='entry-author-name').get_text()
    print("Article Author :",author)

    article_cont = article.find('div',class_ ='entry-content').get_text()
    article_content = article_cont.strip().split('.')[0]
    print("Article Content:",article_content)

    try :
        article_youtube = article.find('iframe', class_= 'youtube-player')['src']
        article_youtube_vedioId =  article_youtube.split('/')[4].split('?')[0]
        article_youtube_vedioLink = 'https://www.youtube.com/watch?v='+article_youtube_vedioId
        print("Article Youtube Link:",article_youtube_vedioLink)
    except Exception as e:
         article_youtube= None

    article_catagory = article.find('a',rel='category tag').get_text()
    print("Article Category :",article_catagory)

    tags = []
    for art_tags in  article.find_all('span',class_='entry-tags'):
        for anh in art_tags.find_all('a'):
            tags.append(anh.get_text())
    print("Article Tags: ",str(tags))

    print("***** **** *****")
    csv_writer.writerow([headline,published_on,author,article_content,article_youtube_vedioLink,article_catagory,tags])
csv_file.close()





#author = article.find(class_ ='entry-author-name').get_text()

#author = article.find(class_ ='entry-author-name').get_text()
#print(author)

