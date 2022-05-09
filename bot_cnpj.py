from xml.dom.minidom import Document
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


class Bot:
    def run(playwright):
        # cnpj = ['02.290.482/0001-97']
        firefox = playwright.firefox
        browser = firefox.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://servicos.receita.fazenda.gov.br/servicos/cnpjreva/Cnpjreva_Solicitacao.asp")

        page.click('#captchaSonoro')

        page.fill("input[name=\"cnpj\"]", "02.290.482/0001-97")
        page.click("input[name=\"cnpj\"]")
        page.click("button:has-text(\"Consultar\")")

        html = page.inner_html('#principal')
        print(html)

             
    with sync_playwright() as playwright:
        run(playwright)