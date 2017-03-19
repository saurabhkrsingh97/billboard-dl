#!usr/bin/env python3

import os
import sys
import pafy
import requests
from bs4 import BeautifulSoup

# For some reason, the latest pafy v0.5.3.1 doesn't work properly, using v0.5.2 here...

# Change TOP_N variable to control how many songs to download
TOP_N = 5


def check_folder(xyz):
    if os.path.isdir(xyz):
        return True
    else:
        os.mkdir(xyz)
        return False


def search_youtube(search_term):
    base_url = 'https://www.youtube.com/results?search_query='
    full_url = base_url + search_term + "&sp=EgIQAQ%253D%253D"
    # Last term needed for video-only search

    r = requests.get(full_url)
    data = r.content

    soup = BeautifulSoup(data, 'html.parser')

    yt_partial_link = soup.find('h3', {'class': 'yt-lockup-title'}).a["href"]
    yt_full_link = 'https://www.youtube.com' + yt_partial_link

    return yt_full_link


def crawl_billboard(n):
    billboard_url = 'http://www.billboard.com/charts/hot-100'
    top_n_songs = ''

    r = requests.get(billboard_url)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')

    all_songs = soup.find_all('div', {'class': 'chart-row__title'})
    songs = all_songs[:n]

    for song in songs:
        temp = song.text.strip()
        t1, t2 = [x.strip() for x in temp.split("\n\n")]
        top_n_songs += str(t1) + ' - ' + str(t2) + '\n'

    # Returns [list of songs, billboard week]
    return [str(top_n_songs), str(soup.find('nav', {'id': 'chart-nav'}).text).strip()]


if __name__ == '__main__':
    dl_enabled = True
    top_n = TOP_N

    if len(sys.argv) > 1:
        top_n = int(sys.argv[1])

    bill_output = crawl_billboard(top_n)
    bill_list = bill_output[0].strip().split('\n')
    bill_week = bill_output[1].strip()

    if dl_enabled:
        check_folder(r'./Billboard/')
        os.chdir(r'./Billboard/')
        check_folder('./' + bill_week + '/')
        os.chdir('./' + bill_week + '/')

    counter = 1
    for item in bill_list:
        print(str(counter) + '.', item)
        link = search_youtube(item)
        print(' [ Link -', link, ']')

        video = pafy.new(link)

        # print(video.description)

        best = video.getbest('mp4')

        item = item.replace('/', '|')  # Handle invalid file names
        if (not os.path.isfile('./' + item + '.mp4')) & dl_enabled:
            best.download(filepath='./' + item + '.mp4')

        counter += 1
