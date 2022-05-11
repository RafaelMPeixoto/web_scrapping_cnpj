from cgitb import text
from xml.dom.minidom import Document
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd


class Bot:
    def run(playwright):

        empresa = {}

        # cnpj = ['02.290.482/0001-97']
        firefox = playwright.firefox
        browser = firefox.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://servicos.receita.fazenda.gov.br/servicos/cnpjreva/Cnpjreva_Solicitacao.asp")

        page.click('#captchaSonoro')

        page.fill("input[name=\"cnpj\"]", "02.290.482/0001-97")
        page.click("input[name=\"cnpj\"]")
        page.click("button:has-text(\"Consultar\")")

        empresa['Matriz'] = page.inner_text ('#principal > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > font:nth-child(3) > b:nth-child(3)')
        
    

        print(empresa)


    with sync_playwright() as playwright:
        run(playwright)
        