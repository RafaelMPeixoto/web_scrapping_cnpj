from ast import Div
from cgitb import text
from gettext import find
from posixpath import split
from re import T
from subprocess import list2cmdline
from xml.dom.minidom import Document
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup, Tag
import pandas as pd

class Bot:
    def run(playwright):

        firefox = playwright.firefox
        browser = firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://servicos.receita.fazenda.gov.br/servicos/cnpjreva/Cnpjreva_Solicitacao.asp")

        page.click('#captchaSonoro')

        page.fill("input[name=\"cnpj\"]", "02.421.421/0001-11")
        page.click("input[name=\"cnpj\"]")
        page.click("button:has-text(\"Consultar\")")
        
        html = page.inner_html('#principal')
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.get_text('b')

        table = table.replace(' ',' ').replace('\t','').replace('\xa0','').replace('\n','').replace('b',' ')

    # def extrair(table, page):

        numero_inscricao = table.split('NÚMERO DE INSCRIÇÃO')[1][4:24].strip()
        data_abertura = table.split('DATA DE ABERTURA')[1][4:28].strip()
        nome_empresarial = table.split('NOME EMPRESARIAL')[1][4:55].strip()
        logradrouro = table.split('LOGRADOURO')[1][4:93].strip()
        numero = table.split('NÚMERO    ')[1][0:15].strip()  
        cep = table.split('CEP')[1][4:23].strip()
        bairro = table.split('BAIRRO/DISTRITO')[1][4:63].strip()
        municipio = table.split('MUNICÍPIO')[1][4:63].strip()
        uf = table.split('UF')[1][4:20].strip()
        email = table.split('ENDEREÇO ELETRÔNICO')[1][4:128].strip()
        fone = table.split('TELEFONE')[1][4:32].replace(' ','').strip()

        dados = (numero_inscricao,
                 data_abertura,
                 nome_empresarial,
                 logradrouro,
                 numero,
                 cep,
                 bairro,
                 municipio,
                 uf,
                 email,
                 fone)
        
        print(f'Número de Inscrição: {dados[0]}'
            '\n'f'Data de abertura: {dados[1]}'
            '\n'f'Nome da Empresa: {dados[2]}'
            '\n'f'Endereço: {dados[3]}'
            '\n'f'Número: {dados[4]}'
            '\n'f'CEP: {dados[5]}'
            '\n'f'Bairro: {dados[6]}'
            '\n'f'Municipio: {dados[7]}'
            '\n'f'UF: {dados[8]}'
            '\n'f'E-mail: {dados[9]}'
            '\n'f'Fone: {dados[10]}')

        
        page.locator("text=Consultar QSA").click()

        html = page.inner_html('#principal')
        soup = BeautifulSoup(html, 'lxml')
        capital = soup.find('div', id='capital').text
        quadroSocios = soup.find(class_='alert alert-warning').text
        soup.findAll('div',string="Nome/Nome Empresarial:")

        # nomeEmpresarial = 
        # qualificacao = 

        # div = soup.find('div').getText().replace('\n', ' ').replace('\t', ' ').replace('\xa0', ' ')

    with sync_playwright() as playwright:
        run(playwright)
        # extrair(playwright)
