from bs4 import BeautifulSoup
import requests

keyword = str(input("Put your Keyword:"))

res = requests.get('https://www.youtube.com/results?search_query=' + keyword + '&sp=EgIIAQ%253D%253D')
soup = BeautifulSoup(res.text, 'html.parser')

results = soup.find_all('a',{'class':'yt-uix-tile-link'})
for link in results:
        href = link["href"]
        if href.startswith('/channel') | href.startswith('/user'):
                href = ""
        else:
                newhref = 'https://www.youtube.com' + href + '\n'
                f = open("url.txt", "a")
                f.write(newhref)
                f.close()


