import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

hn_links = soup.select('.storylink')
hn_subtext = soup.select('.subtext')


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


data = create_custom_hn(hn_links, hn_subtext)
pprint.pprint(data)

# print(soup.body)  # returns the body of the page
# print(soup.body.contents)  # returns contents in body as list

# print(soup.find_all('div'))  # retuns all the divs as a list
# print(soup.find(id="score_20514755"))  # find element by id
