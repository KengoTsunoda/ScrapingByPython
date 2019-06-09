from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

# サイトのページのパターンを見つける
pages = set()
def getlinks(pageUrl):
    global pages
    html = urlopen('https://')
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').find_all('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')

    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 新しいページに出会った
                newpage = link.attrs['href']
                print('-'*20)
                print(newpage)
                pages.add(newpage)
                getlinks(newpage)

getlinks('')