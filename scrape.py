import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

hn_links = soup.select('.storylink')
hn_votes = soup.select('.score')


def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        points = int(votes[index].getText().replace(' points', ''))
        print(points)
        hn.append({'title': title, 'link': href})
    return hn


create_custom_hn(hn_links, hn_votes)

# print(soup.body)  # returns the body of the page
# print(soup.body.contents)  # returns contents in body as list

# print(soup.find_all('div'))  # retuns all the divs as a list
# print(soup.find(id="score_20514755"))  # find element by id
