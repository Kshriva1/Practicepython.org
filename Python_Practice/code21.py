import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input("Enter the url")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup.findAll('p')
with open("file1.txt",'w') as open_file:
    for tag in tags:
        open_file.write(tag.text.replace("\n"," ").strip())
