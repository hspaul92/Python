# Tribute to : Corey M Schafer
# This is developed only for learning purpose .
#
import requests
from bs4 import BeautifulSoup
import csv

# Csv Page Layout
csv_file =open('scrap_data_CoreySchafer_Page.csv','w',newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['HeadLine','Published On','Author','Content','YouTube','Category','Tags','Page No','Page Link'])

# Build URL
base_page='https://coreyms.com/'
url=''
for i in range (1,18):
    if i== 1:
        url=base_page
    else:
       url = base_page+'page/'+str(i)
    print("Page :",i," :",url)


    # Request the page
    source = requests.get(url).text
    soup   =  BeautifulSoup(source,'lxml')
    #print(soup.prettify())
    for article in soup.find_all('article'):
        # print(article.prettify())
        print("***** **** *****")

        headline = article.h2.a.text
        print(headline)

        published_on = article.find('time', class_='entry-time').get_text()
        print("Article Published On :", published_on)

        author = article.find('span', class_='entry-author-name').get_text()
        print("Article Author :", author)

        article_cont = article.find('div', class_='entry-content').get_text()
        article_content = article_cont.strip().split('.')[0]
        print("Article Content:", article_content)

        try:
            article_youtube = article.find('iframe', class_='youtube-player')['src']
            article_youtube_vedioId = article_youtube.split('/')[4].split('?')[0]
            article_youtube_vedioLink = 'https://www.youtube.com/watch?v=' + article_youtube_vedioId
            print("Article Youtube Link:", article_youtube_vedioLink)
        except Exception as e:
            article_youtube = None

        article_catagory = article.find('a', rel='category tag').get_text()
        print("Article Category :", (article_catagory))

        tags = []
        for art_tags in article.find_all('span', class_='entry-tags'):
            for anh in art_tags.find_all('a'):
                tags.append(anh.get_text())
        print("Article Tags: ", str(sorted(tags)))

        print("***** **** *****")
        csv_writer.writerow(
            [headline, published_on, author, article_content, article_youtube_vedioLink, article_catagory, tags,i,url])


csv_file.close()

