import requests
from bs4 import BeautifulSoup
import operator

def start(url):         # start is not a specific name , you can give any name also
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,  "html.parser")
    for post_next in soup.findAll('h3', {'class':'_eYtD2XCVieq6emjKBH3m'}):
        content = post_next.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)

start('https://www.reddit.com/r/NoFap/')