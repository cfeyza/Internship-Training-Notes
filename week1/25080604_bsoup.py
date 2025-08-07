html_doc = open("C:/Users/FEYZA/OneDrive/Belgeler/python_august/week1/25080603_htmlbasics.html", "r", encoding='utf8').read()
#BeautifulSoup : Verilen HTML içeriğini analiz etmek için kullanılır
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser',)
result = soup.prettify()
print(result)
print(soup.title)
print(soup.head)
print(soup.body)
print(soup.title.name)
print(soup.title.string)
print(soup.h1)
print(soup.h2) #ilk h2 yi getirir
print(soup.h2.name)
print(soup.h2.string)
print(soup.h1.string)
print(soup.find_all('h2'))
print(soup.find_all('h2')[1])
print(soup.div) # ilk div gelir
print(soup.find_all('div')[1])
print(soup.find_all('div')[1].ul)
print(soup.find_all('div')[1].ul.find_all('li'))
print(soup.div.findChildren) #ilk divin tüm alt ögeleri
print(soup.div.next_sibling)
print(soup.div.previous_sibling)
res = soup.findAll('a')
for link in res:
    print(link)
    print(link.get("href"))

