import requests
from bs4 import BeautifulSoup
import pprint
import sys


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext, output):
    hn = output
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def scrape(pages):
    output = []
    for page in range(1, int(pages) + 1):
        res = requests.get(f'https://news.ycombinator.com/news?p={str(page)}')
        soup = BeautifulSoup(res.text, 'html.parser')

        hn_links = soup.select('.storylink')
        hn_subtext = soup.select('.subtext')

        create_custom_hn(hn_links, hn_subtext, output)
    return output


data = scrape(sys.argv[1])
pprint.pprint(data)

# print(soup.body)  # returns the body of the page
# print(soup.body.contents)  # returns contents in body as list

# print(soup.find_all('div'))  # returns all the divs as a list
# print(soup.find(id="score_20514755"))  # find element by id
