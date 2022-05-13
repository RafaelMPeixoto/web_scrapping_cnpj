from cgitb import text
from gettext import find
from posixpath import split
from xml.dom.minidom import Document
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup, Tag
import pandas as pd


class Bot:
    def run(playwright):
        firefox = playwright.firefox
        browser = firefox.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://servicos.receita.fazenda.gov.br/servicos/cnpjreva/Cnpjreva_Solicitacao.asp")

        page.click('#captchaSonoro')

        page.fill("input[name=\"cnpj\"]", "02.290.482/0001-97")
        page.click("input[name=\"cnpj\"]")
        page.click("button:has-text(\"Consultar\")")
        html = page.inner_html('#principal')
        
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.get_text('b')


        table = table.replace(' ',' ').replace('\t','').replace('\xa0','').replace('\n','').replace('b',' ')

        numero_inscricao = table.split('NÚMERO DE INSCRIÇÃO')[1][4:24].strip()
        data_abertura = table.split('DATA DE ABERTURA')[1][4:28].strip()
        nome_empresarial = table.split('NOME EMPRESARIAL')[1][4:55].strip()
        titulo_estabelacimento = table.split('TÍTULO DO ESTABELECIMENTO (NOME DE FANTASIA)')[1][4:69].strip()
        


        # numero_inscricao = table.split('NÚMERO DE INSCRIÇÃO') # split retorna uma lista
        # numero_inscricao = numero_inscricao[1]
        # numero_inscricao = numero_inscricao[4:22]


    with sync_playwright() as playwright:
        run(playwright)
        
        
        
        