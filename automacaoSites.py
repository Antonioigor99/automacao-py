import pyautogui
from time import sleep

#realizar requisicoes para o servidor
import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.kabum.com.br/?gad_source=1&gclid=Cj0KCQiAy9msBhD0ARIsANbk0A-XbpaJ624ynbEhQ5ZhyOrHgTXvUxclVgP0rxkvgCfl4Op56wx-8o0aAoPxEALw_wcB')
#####
#variavel contendo todo conteudo html da pagina
contentHtml = response.content

#transformando a var com conteudo em um objeto e validando o html dele
site = BeautifulSoup(contentHtml, 'html.parser')
#print(site.prettify()) : para chamar o html mais organizado.

#criando uma variavel da div onde contem as informacoes que preciso.
CardKabum = site.find('div', attrs={'class': 'productCard'})

#titulo da pagina 'string'
titulo = CardKabum.find('span', attrs={'class': 'nameCard'})
print(titulo.text)

preco = CardKabum.find('span', attrs={'class': 'oldPriceCard'})
print(preco.prettify())


