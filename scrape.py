import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')
votes = soup.select('.score')


# print(soup.body)  # returns the body of the page
# print(soup.body.contents)  # returns contents in body as list

# print(soup.find_all('div'))  # retuns all the divs as a list
# print(soup.find(id="score_20514755"))  # find element by id
