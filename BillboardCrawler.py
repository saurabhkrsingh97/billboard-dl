#!usr/bin/env python3

import requests
from bs4 import BeautifulSoup

billboard_url = 'http://www.billboard.com/charts/hot-100'


def bill(top_n=20):
    top_n_songs = ''
    r = requests.get(billboard_url)
    data = r.content
    soup = BeautifulSoup(data)
    all_songs = soup.find_all('div', {'class': 'chart-row__title'})
    songs = all_songs[:top_n]
    for song in songs:
        top_n_songs += song.h2.text + ' - ' + str(song.h3.text).strip() + '\n'
    # print(top_n_songs)
    return [str(top_n_songs), str(soup.find('nav', {'id': 'chart-nav'}).text).strip()]

# bill(10)
