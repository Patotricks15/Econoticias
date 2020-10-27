# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 06:19:14 2020

@author: Patrick Gomes (Patotricks15)
"""

from bs4 import BeautifulSoup
import requests

def g1():
  url =  'https://g1.globo.com/economia/'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')

  print(f'\n\n                    G1 - ECONOMIA ({url})\n\n')
  noticia_lista = soup.find_all('a', class_= 'feed-post-link gui-color-primary gui-color-hover', href=True)
  horario_lista = soup.find_all('span', class_='feed-post-datetime')
  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('>')[1][:-3]
    horario = str(horario_lista[i]).split('>')[1][:-6]
    link = str(noticia_lista[i]).split('"')[3]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def bbc_br():
  url =  'https://www.bbc.com/portuguese/topics/cvjp2jr0k9rt'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    BBC BRASIL - ECONOMIA ({url})\n\n')


  noticia_lista = soup.find_all('span',  class_="lx-stream-post__header-text gs-u-align-middle")
  horario_lista = soup.find_all('span', class_="qa-post-auto-meta")
  link_lista = soup.find_all('a',  class_="qa-heading-link lx-stream-post__header-link", href=True)
  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('>')[1][:-6]
    horario = str(horario_lista[i]).split('>')[1][:-6]
    link = 'www.bbc.com' + str(link_lista[i]).split('href="')[1].split('">')[0]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def nexo():
  url =  'https://www.nexojornal.com.br/tema/Economia'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    NEXO JORNAL - ECONOMIA ({url})\n\n')

  noticia_lista = soup.find_all('h4',  class_="Teaser__title-dark___1HEzZ")
  horario_lista = soup.find_all('span', class_="qa-post-auto-meta")
  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('alt="')[1].split('" href="')[0]
    link =  str(noticia_lista[i]).split('" href="')[1].split('" title="')[0]
    link_final = 'www.nexojornal.com.br' + link
    print(f'\n\n{noticia}\n{link_final}\n')

#_______________________________________________________________________________________________________________________
def valor():
  url =  'https://valor.globo.com/busca/?q=economia&page=1'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    VALOR ECONÔMICO ({url})\n\n')


  noticia_lista = soup.find_all('div',  class_="widget--info__title product-color ")
  horario_lista = soup.find_all('div', class_="widget--info__meta")
  link_lista = soup.find_all('a')
  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('>')[1][:-7].split('\n')[1]
    horario = str(horario_lista[i]).split('>')[1][:-5]
    link = str(link_lista[i]).split('<div')[0].split('"')[1]
    print(f'\n{noticia}\n          {horario}\n')

#_______________________________________________________________________________________________________________________
def bloomberg_br():
  url =  'https://www.bloomberg.com.br/blog/category/noticias-exclusivas/'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    BLOOMBERG Brasil - ECONOMIA({url})\n\n')


  noticia_lista = soup.find_all('h3', class_="h3-regular-8")
  horario_lista = soup.find_all('div', class_="widget--info__meta")
  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('">')[2].split('</a>')[0]
    link = str(noticia_lista[i]).split('href="')[1].split('">')[0]
    print(f'\n{noticia}\n{link}\n')

#_______________________________________________________________________________________________________________________
def infomoney():
  url =  'https://www.infomoney.com.br/ultimas-noticias/'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                   INFOMONEY ({url})\n\n')


  noticia_lista = soup.find_all('span', class_="hl-title hl-title-2")
  horario_lista = soup.find_all('span',  class_="posted-diff")
  for i in range(len(noticia_lista[:8])):
    noticia = str(noticia_lista[i]).split('title="')[1].split('</a>')[0].split('">')[0]
    link = str(noticia_lista[i]).split('href="')[1].split('" title')[0]
    horario = str(horario_lista[i]).split('">')[1].split('</span>')[0]
    print(f'\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def valorinveste():
  url =  'https://valorinveste.globo.com/ultimas-noticias/'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    VALOR INVESTE ({url})\n\n')


  noticia_lista = soup.find_all('a', class_="feed-post-link gui-color-primary gui-color-hover")
  horario_lista = soup.find_all('span',  class_="feed-post-datetime")

  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('">')[1].split('</a>')[0]
    link = str(noticia_lista[i]).split('href="')[1].split('">')[0]
    horario = str(horario_lista[i]).split('">')[1].split('</span>')[0]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def braziljournal():
  url =  'https://braziljournal.com/categoria/economia'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    BRAZILJOURNAL - ECONOMIA ({url})\n\n')

  noticia_lista = soup.find_all('a', class_="article-title")
  horario_lista = soup.find_all('div',  class_="article-date")

  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('href="')[1].split('">')[1][:-4]
    link = str(noticia_lista[i]).split('href="')[1].split('">')[0]
    horario = str(horario_lista[i]).split('">')[1].split('</div>')[0]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def exame():
  url =  'https://exame.com/economia/'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    EXAME - ECONOMIA ({url})\n\n')

  noticia_lista = soup.find_all('span', class_="list-item-title")
  horario_lista = soup.find_all('span',  class_="list-date-description")
  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('title="')[1].split('">')[0]
    link = str(noticia_lista[i]).split('href="')[1].split('" title=')[0]
    horario = str(horario_lista[i]).split('">')[1].split('</span>')[0]

    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def estadao():
  url =  'https://economia.estadao.com.br/'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    ESTADÃO - ECONOMIA ({url})\n\n')

  noticia_lista = soup.find_all('section', class_="col-md-12 col-sm-12 col-xs-12 init item-lista")
  horario_lista = soup.find_all('span',  class_="list-date-description")
  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('" title=')[7].split('> <h3 class="third">')[0][1:][:-1]
    link = str(noticia_lista[i]).split('data-href="')[1].split('data-title=')[0]
    horario = str(noticia_lista[i]).split('class="data-posts">')[1].split('</span>')[0]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')
    
#_______________________________________________________________________________________________________________________
def ibre():
  url =  'https://blogdoibre.fgv.br/'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    BLOG DO IBRE(FGV) ({url})\n\n')


  noticia_lista = soup.find_all('div', class_="views-field views-field-title", href=False)
  horario_lista = soup.find_all('div', class_="views-field views-field-nothing-1")
  for i in range(len(noticia_lista[:10])):
    noticia = str(noticia_lista[i]).split('">')[3].split('</a>')[0]
    link = 'https://blogdoibre.fgv.br' + str(noticia_lista[i]).split('href="')[1].split('</a>')[0].split('">')[0]
    horario = str(horario_lista[i]).split('single">')[1].split('</span>')[0]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def vox():
  url =  'https://www.vox.com/search?q=economy'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    VOX - ECONOMY ({url})\n\n')

  noticia_lista = soup.find_all('h2', class_="c-entry-box--compact__title")
  horario_lista = soup.find_all('time',  class_="c-byline__item")

  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('">')[2][:-(len('</a></h2>'))]
    link = str(noticia_lista[i]).split('href="')[1].split('">')[0]
    horario = str(horario_lista[i]).split('">')[1].split('\n')[1][len('          '):]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def fintimes():
  url =  'https://www.ft.com/search?q=economy&sort=date'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    FINANCIAL TIMES - ECONOMY ({url})\n\n')

  noticia_lista = soup.find_all('div', class_="o-teaser__heading")
  horario_lista = soup.find_all('time',  class_="o-teaser__timestamp-date")

  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('">')[2].split('</a')[0]
    link = 'www.ft.com' + str(noticia_lista[i]).split('href="')[1].split('">')[0]
    horario = str(horario_lista[i]).split('">')[1][:-len('</time>')]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def nytimes():
  url =  'https://www.nytimes.com/search?query=economy'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    THE NEW YORK TIMES - ECONOMY ({url})\n\n')

  noticia_lista = soup.find_all('div', class_="css-e1lvw9")
  horario_lista = soup.find_all('span', class_="css-bc0f0m")
  for i in range(len(noticia_lista[:4])):
    link = 'www.nytimes.com' + str(noticia_lista[i]).split('href="')[1].split('"><h4')[0]
    noticia = str(noticia_lista[i]).split('4k">')[1].split('</h')[0]
    horario = str(horario_lista[i]).split('</span>')[2].split(', P')[0]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

#_______________________________________________________________________________________________________________________
def bbc():
  url =  'https://www.bbc.co.uk/search?q=economy&page=1'
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  print(f'\n\n                    BBC - ECONOMY ({url})\n\n')

  noticia_lista = soup.find_all('div', class_="css-v4rel9-PromoContent e1f5wbog0")
  horario_lista = soup.find_all('div', class_="css-3r6h34-PromoContentMetadata e1f5wbog6")
  for i in range(len(noticia_lista)):
    noticia = str(noticia_lista[i]).split('"false">')[1].split('</span>')[0]
    horario = str(horario_lista[i]).split('aria-hidden="false">')[1].split('</span>')[0]
    link = str(noticia_lista[i]).split('href="')[1].split('"><span')[0]
    print(f'\n\n{noticia}\n{horario}\n{link}\n')

midias = {
  'g1': g1,
  'bbc_br': bbc_br,
  'nexo': nexo,
  'valor': valor,
  'valorinveste': valorinveste,
  'bloomberg_br': bloomberg_br,
  'infomoney': infomoney,
  'braziljournal': braziljournal,
  'exame': exame,
  'estadao': estadao,
  'ibre': ibre,
  'vox': vox,
  'fintimes': fintimes,
  'nytimes': nytimes,
  'bbc': bbc
}

while True:
    jornal = input('________________________________________________________________\nEscolha o jornal de sua preferência\n(g1, bbc_br, nexo, valor, valorinveste, bloomberg_br, infomoney, braziljournal, exame, estadao, ibre, vox, fintimes, nytimes, bbc)\n[q] para sair\n_________________________________________________________________\n>>>')
    if jornal in midias:
      midias[jornal]()
    elif jornal == 'q':
      break
    else:
      print('Insira uma mídia válida')
