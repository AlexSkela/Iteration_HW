import json

import requests

from pprint import pprint

from bs4 import BeautifulSoup

with open("countries.json", encoding='utf-8') as c:
    country = json.load(c)

    # pprint(country)

country_list = []

for name in country:
    for n in name:
        n = name['name']['common']
        country_list.append(n)
        country_set = set(country_list)
# pprint(country_set)

URL = 'https://en.wikipedia.org/wiki/List_of_sovereign_states'

class MyIteration:

    # URL = 'https://en.wikipedia.org/wiki/List_of_sovereign_states'

    def __init__(self, name_country):
        self.name_country = name_country

    def get_href(self, URL):
        response = requests.get(f'{URL}')
        if not response.ok:
            raise Exception('запрос неверный')

        text = response.text

        soup = BeautifulSoup(text, features="html.parser")

        text = soup.find_all('tbody')

        # pprint(text)


        for name in text:
            hrefs = name.find_all('b')
            for names in hrefs:
                title = names.find_all('a')
                for m in title:
                    con = m.attrs.get('title')
                    con_list = []
                    con_list.append(con)
                    con_set = set(con_list)


                    # pprint(con_set)

                    if con_set & self.name_country:
                        resault = m.attrs.get('href')
                        print(con, resault)
#
#
#     def __iter__(self):
#         self.cursor = 0
#         return self
#
#     def __next__(self):

count = MyIteration(country_set)

count.get_href(URL)