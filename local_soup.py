from bs4 import BeautifulSoup as soup
from local_soup_modulo import ExecutarModulo1

def ConstrutorSoup():
	endereco_html = open ("C:/Users/erick/Documents/codes/Selenium e Beautiful Soup/local_soup_html.html", "r")
	site_local = endereco_html.read()

	local_soup = soup(site_local, 'html.parser')
	return local_soup

#-------------------------------------------------------------------------------------------------------
ExecutarModulo1 () #uma vez executado o código, coloque esta linha como comentário
local_soup = ConstrutorSoup()

pesquisa1 = local_soup.find_all ("a", class_ = "recent-song__name")
pesquisa2 = local_soup.find_all ("div", class_ = "recent-song__anime")
pesquisa3 = [i.find ("a") for i in pesquisa2]

x = 0
for i in pesquisa1:
	print ("song:", pesquisa1[x].get_text().strip ())
	print ("from:", pesquisa3[x].get_text().strip ())
	print ("\n")
	x+=1