import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.pyclass.com/example.html",
                        headers={
                            'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

content = response.content
soup = BeautifulSoup(content, 'html.parser')
cities = [h.text for div in soup.find_all('div', {'class': 'cities'}) for h in div.find_all('h2')]
print(cities)