import pygeoip      # for working with geographical locations connected to ip address
import requests    # for requesting urls data
from bs4 import BeautifulSoup   # help scrape or find the information u need from the web page source


plain_text = requests.get('https://www.myip.com/').text     # this website gives your ip address and nothing else
soup = BeautifulSoup(plain_text, "html.parser")
for link in soup.findAll("span", {'id': "ip"}):
    my_ip_addr = link.string

print(my_ip_addr)

gip = pygeoip.GeoIP('GeoLiteCity.dat')          # storing database file in variable gip
res = gip.record_by_addr(my_ip_addr)

for key,value in res.items():
    print(f'{key} : {value} ')