# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# try:
#     html = urlopen('http://www.pythonscraping.com/pages/page3.html')
#     bs = BeautifulSoup(html, 'html.parser')

#     print(bs.find('img',
#     {'src':'../img/gifts/img1.jpg'})
#     .parent.previous_sibling.get_text())

# except:
#     print('Site nao encontrado')

# for child in bs.find('table',{'id':'giftList'}).children:

#     print(child)



# valor = bs.find_all(id= 'gift1')

# print(valor)


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',{'src':'../img/gifts/img2.jpg'}).parent.previous_sibling.get_text())