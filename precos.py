import requests
from bs4 import BeautifulSoup


def produtos(link):
    final = []
    for produto in link:
        url = produto
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')
        roupa = soup.find("div",class_='goods-name')
        roupa = roupa.text
        final.append(roupa)
        preco = soup.find('div', class_='goods-price__wrapper')
        preco = preco.text
        final.append(f'{preco}\n \n')
        final.append(f'site: {url}\n'+'-'*90)
    with open('precos_de_roupas.txt', 'w') as arquivo:
        for valores in final:
            arquivo.write(str(valores))

sites = []

with open('url.txt', 'r') as fonte:
    for urls in fonte:
        sites.append(urls)

produtos(sites)

