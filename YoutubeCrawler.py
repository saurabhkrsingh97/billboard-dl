#!usr/bin/env python3

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.youtube.com/results?search_query='


def youtube(search_term='Coldplay'):
    full_url = base_url + search_term + '&sp=EgIQAQ%253D%253D'
    r = requests.get(full_url)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    yt_partial_link = soup.find('div', {'class': 'yt-lockup-content'}).h3.a['href']
    yt_full_link = 'https://www.youtube.com' + yt_partial_link
    # print(yt_full_link)
    return yt_full_link
