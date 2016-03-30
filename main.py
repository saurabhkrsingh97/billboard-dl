#!usr/bin/env python3

from BillboardCrawler import *
from YoutubeCrawler import *
from CheckDir import *
import pafy
import sys

dl_enabled = True
top_n = 5
if len(sys.argv) > 1:
    top_n = int(sys.argv[1])

bill_output = bill(top_n)
bill_list = bill_output[0].strip().split('\n')
bill_week = bill_output[1].strip()

if dl_enabled:
    check_dir(r'./Billboard/')
    os.chdir(r'./Billboard/')
    check_dir('./' + bill_week + '/')
    os.chdir('./' + bill_week + '/')

counter = 1
for item in bill_list:
    print(str(counter) + '.', item)
    link = youtube(item)
    print(' [ Link -', link, ']')
    video = pafy.new(link)
    best = video.getbest('mp4')
    # print(video.description)
    if (not os.path.isfile('./' + item + '.mp4')) & dl_enabled:
        best.download(filepath='./' + item + '.mp4')
    counter += 1
    print('\n')
