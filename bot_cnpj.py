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

        page.fill("input[name=\"cnpj\"]", "10.931.607/0001-49")
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
        titulo_estabelecimento = table.split('TÍTULO DO ESTABELECIMENTO (NOME DE FANTASIA)')[1][4:69].strip()
        logradrouro = table.split('LOGRADOURO')[1][4:93].strip()
        numero = table.split('NÚMERO    ')[1][0:15].strip()  
        cep = table.split('CEP')[1][4:23].strip()
        bairro = table.split('BAIRRO/DISTRITO')[1][4:63].strip()
        municipio = table.split('MUNICÍPIO')[1][4:63].strip()
        uf = table.split('UF')[1][4:20].strip()
        email = table.split('ENDEREÇO ELETRÔNICO')[1][4:128].strip()
        fone = table.split('TELEFONE')[1][4:32].replace(' ','').strip()

        dados1 = ([numero_inscricao],
                  [data_abertura],
                  [nome_empresarial],
                  [titulo_estabelecimento],
                  [logradrouro],
                  [numero],
                  [cep],
                  [bairro],
                  [municipio],
                  [uf],
                  [email],
                  [fone])
        
        print(f'Número de Inscrição: {numero_inscricao}'
            '\n'f'Data de abertura: {data_abertura}'
            '\n'f'Nome da Empresa: {nome_empresarial}'
            '\n'f'Título do Estabelecimento: {titulo_estabelecimento}'
            '\n'f'Endereço: {logradrouro}'
            '\n'f'Número: {numero}'
            '\n'f'CEP: {cep}'
            '\n'f'Bairro: {bairro}'
            '\n'f'Municipio: {municipio}'
            '\n'f'UF: {uf}'
            '\n'f'E-mail: {email}'
            '\n'f'Fone: {fone}')

        
        # page.locator("text=Consultar QSA").click()

        # html = page.inner_html('#principal')
        # soup = BeautifulSoup(html, 'html.parser')
        # table = soup.get_text('div')

        # table = table.replace('\ndiv',' ').replace('\t',' ').replace('\n',' ').replace('\xa0div',' ').replace('div',' ') 
        
        # cnpj = table.split('CNPJ')[1][3:25].strip()
        # nome_empresarial1 = table.split('NOME EMPRESARIAL')[1][3:157].strip()
        # capital_social = table.split('CAPITAL SOCIAL')[1][3:39].strip()

        # nome_empresarial2 = table.split('Nome/Nome Empresarial')[1][1:151].strip()
        # qualificacao = table.split('Qualificação')[1][1:23].strip()

        # nome_empresarial3 = table.split('Nome Empresarial')   

    with sync_playwright() as playwright:
        run(playwright)
        # extrair(playwright)
            
    
                    
        
        
        
        