from cgitb import text
from gettext import find
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

        # table = table.replace(' ',' ').replace('\t','').replace('\xa0','').replace('\n','')
             
    with sync_playwright() as playwright:
        run(playwright)
        
        
        
        