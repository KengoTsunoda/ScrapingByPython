from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        # 第一引数：HTMLテキスト、第二引数：パーサを指定（'lxml', 'html5lib'などがある）
        bs = BeautifulSoup(html.read(), 'html.parser')
        # find_all(tagName, tagAttributes) → 再帰的（recursive）に動作する。
        nameList = bs.find_all('span', {'class' : {'green', 'red'}})
        for name in nameList:
            print(name.get_text())
        title = bs.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title

title = getTitle('https://shop-healthcare.fujifilm.jp/')
if title == None:
    print('Title could not be found')
else:
    print(title)