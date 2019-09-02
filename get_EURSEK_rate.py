import requests
from bs4 import BeautifulSoup

def get_EURSEK_rate():
	"""Extract live EURSEK rate form investing.com"""

	URL = 'https://www.investing.com/currencies/eur-sek'
	file_name = 'EURSEK Rate' + '.xlsx'
	folder_path = r'C:\Users\Vartotojas\Desktop'
	file_path = folder_path + '\\' + file_name

	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	SEK_rate = soup.find(id="last_last").get_text()

	print('SEK price - ' + str(SEK_rate) + '\n\n')

	return SEK_rate
