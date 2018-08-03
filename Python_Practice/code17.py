import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input("Enter the url")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup.findAll('p')
for tag in tags:
    print(tag.text.replace("\n"," ").strip())
