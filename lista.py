import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd


city = []
date = []
description = []


class ScrapyShopee:
    def __init__(self):
        self.url = f'https://www.vagas.com.br/vagas-de-python?'

        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, 'html.parser')

    def busca(self):
        self.vaga_emprego = self.soup.find_all(
            'div', {'class': 'informacoes-header'})

        for vaga_empregos in self.vaga_emprego:
            pegar_dados = vaga_empregos.find_all('a')

            title = [pegar_dado['title'] for pegar_dado in pegar_dados]

            href = [
                f'https://www.vagas.com.br/vagas-de-{pegar_dado["href"]}?' for pegar_dado in pegar_dados]

    def busca_cidade(self):
        cidades = self.soup.find_all('span', {'class': 'vaga-local'})
        for cidade in cidades:
            city.append(cidade.text.replace('\n', '').replace(' ', ''))

    def busca_data(self):
        datas = self.soup.find_all('span', {'class': 'data-publicacao'})
        for data in datas:
            date.append(data.text)

    def busca_descricao(self):
        descricoes = self.soup.find_all('div', {'class': 'detalhes'})
        for descricao in descricoes:
            description.append(descricao.text)


if __name__ == '__main__':
    shopee = ScrapyShopee()
    shopee.busca()
    shopee.busca_cidade()
    shopee.busca_data()
    shopee.busca_descricao()
    print(title)
    print(href)

'''
    dicionario = {
        'nome da vaga': title,
        'Descrição': description,
        'urls': href,
        'cidade': city,
        'data': date

    }

    r = pd.DataFrame(data=dicionario)
    r.to_excel('vagas.xlsx')
'''
