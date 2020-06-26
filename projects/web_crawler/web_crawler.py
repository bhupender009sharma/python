import requests         # used requesting urls from web pages
from bs4 import BeautifulSoup   # help scrape or find the information u need from the web page source

def spider(max_pages):
    page =1
    while page <= max_pages:
        url= 'https://openlibrary.org/search?q=subject%3A%28%22Reading+Level-Grade+11%22+OR+%22Reading+Level-Grade+12%22%29+first_publish_year%3A%5B2000+TO+%2A%5D&has_fulltext=true&page=' + str(page)
        source_code= requests.get(url)              # get the source code of the url
        plain_text= source_code.text                #get all the text from the sorce_code
        soup = BeautifulSoup(plain_text, "html.parser")   # get the plain_text into the class BeautifulSoup and store it in object soup
                                                          #Parser has to be explicitly specified,so I'm using the best
                                                          #available HTML parser for this system ("html.parser").
                                                          # This usually isn't a problem, but if you run this code on
                                                          # another system, or in a different virtual environment,
                                                          # it may use a different parser and behave differently.
        for link in soup.findAll( "a", {'class' : "results"} ):     # a is the type of line we are looking for
            href =  "https://openlibrary.org" + link.get("href")    # getting href link from the source code
            title = link.string                     # title of the link is  called string
            print(title)
            print(href)
            single_item_data(href)
        page += 1



def single_item_data(item_url):             #this will go to every single item specifically, and then gets its data
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item in soup.findAll('div',{'class':"published"}): #this will get publishing date of the item
        print(item.string)

spider(1)