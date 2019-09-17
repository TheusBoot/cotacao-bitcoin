from bs4 import BeautifulSoup as bs
import time

while True:
	time.sleep(60)
	base_url = 'https://dolarhoje.com/bitcoin-hoje/'
	btc = get(base_url)
	btc_page = bs(btc.text, 'html.parser')

	boxes = btc_page.find_all('input',{'type':'text'},{'id':'nacional'})
	valor = str(boxes[-1])
				
	tipo_de_moeda, valor_final = valor.split('value=')

	print(f'O valor do bitcoin Hoje R$:{valor_final}')#.format(valor_final)
