import requests
import bs4

usuario = 'levinegurgelf'
res = requests.get('https://www.instagram.com/'+usuario+'/')
type(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')

title = soup.select('title')

title[0].getText()

description = soup.find('meta', property="og:description")

print(description)