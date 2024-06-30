from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup 

def Titulo(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1

    except AttributeError as e:
        return None
    return title

title = Titulo('https://www.youtube.com/')
if title == None:
    print('titulo nao foi encontrado')
else:
    print(title)
