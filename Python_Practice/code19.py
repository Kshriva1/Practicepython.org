import bs4, requests
res = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
soup = bs4.BeautifulSoup(res.text, "html5lib")
for lines in soup.find_all('p'):
    print(str(lines.getText()))
