from selenium import webdriver
from bs4 import BeautifulSoup as soup
from time import sleep

def SiteOnline(): #retorna um objeto do tipo Beautiful Soup
	configuracao = webdriver.EdgeOptions()
	configuracao.add_argument ("--start-maximized")
	navegador = webdriver.Edge (options=configuracao)

	site = navegador.get("https://animesongs.org/")
	
	sleep (10)

	site_atual = soup (navegador.page_source, 'html.parser')
	#print (site_atual.prettify())
	return site_atual

def SalvarLocal(site_soup):
	ideia = open ("local_soup_html.html","w")
	ideia.write (site_soup.prettify())
	ideia.close()

def ExecutarModulo1 ():
	este_site = SiteOnline()
	SalvarLocal(este_site)