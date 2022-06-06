from os import access
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
from lista import lista

class Bot:
    def run(playwright, lista):
        elem_atual = lista[0]
        del lista[0]

        firefox = playwright.firefox
        browser = firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://servicos.receita.fazenda.gov.br/servicos/cnpjreva/Cnpjreva_Solicitacao.asp")

        page.click('#captchaSonoro')
        
        page.fill("input[name=\"cnpj\"]", elem_atual)
        page.click("input[name=\"cnpj\"]")
        page.click("button:has-text(\"Consultar\")")
        
        html = page.inner_html('#principal')
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.get_text('b')

        lista_table=(table.replace('\t','').replace('\xa0','').replace('b','')).split('\n')
        while('' in lista_table):
            lista_table.remove('')

        print('\n'f'Número de Inscrição: {lista_table[3].strip()}'
            '\n'f'Data de abertura: {lista_table[7].strip()}'
            '\n'f'Nome da Empresa: {lista_table[9].strip()}'
            '\n'f'Endereço: {lista_table[24].strip()}'
            '\n'f'Número: {lista_table[27].strip()}'
            '\n'f'CEP: {lista_table[32].strip()}'
            '\n'f'Bairro: {lista_table[35].strip()}'
            '\n'f'Municipio: {lista_table[38].strip()}'
            '\n'f'UF: {lista_table[41].strip()}'
            '\n'f'E-mail: {lista_table[43].strip()} {lista_table[44].strip()}'
            '\n'f'Fone: {lista_table[46].strip()}''\n')

        page.locator("text=Consultar QSA").click()

        html = page.inner_html('#principal')
        soup = BeautifulSoup(html, 'lxml')
        capital = soup.find('div', id='capital').text.strip()
        socios = soup.findAll('div', class_="col-md-9")[3:]
        qualificacao = soup.findAll('div', class_="col-md-5")[0:]

        listaCapital=(capital).split('\n')
        while("" in listaCapital) :
            listaCapital.remove("")

        listaSocios = socios[0:]
        listaQualificacao = qualificacao[0:]

        print('\n'f'CNPJ: {listaCapital[1]}'
            '\n'f'NOME EMPRESARIAL: {listaCapital[3]}'
            '\n'f'CAPITAL SOCIAL: {listaCapital[5]}''\n'
            )

        print(f'Nome/Nome Empresarial: {listaSocios[0].text.strip()}'
            '\n'f'Qualificação: {listaQualificacao[0].text.strip()}'
            '\n''\n'
            f'Nome/Nome Empresarial: {listaSocios[1].text.strip()}'
            '\n'f'Qualificação: {listaQualificacao[1].text.strip()}'
            '\n''\n'
            f'Nome/Nome Empresarial: {listaSocios[2].text.strip()}'
            '\n'f'Qualificação: {listaQualificacao[2].text.strip()}'
            '\n''\n'
            )

        browser.close()     

    with sync_playwright() as playwright:
        run(playwright, lista)
        while True:
            run(playwright, lista)
                                
            
