#!usr/bin/env python3

from BillboardCrawler import *
from YoutubeCrawler import *
from CheckDir import *
import pafy

counter = 1
dl_enabled = True
top_n = 3

bill_output = bill(top_n)
bill_list = bill_output[0].strip().split('\n')
bill_week = bill_output[1].strip()

if dl_enabled:
    check_dir(r'./Billboard/')
    os.chdir(r'./Billboard/')
    check_dir('./' + bill_week + '/')
    os.chdir('./' + bill_week + '/')

for item in bill_list:
    print(str(counter) + '.', item)
    link = youtube(item)
    print('[ Link -', link, ']')
    video = pafy.new(link)
    best = video.getbest('mp4')
    # print(video.description)
    if (not os.path.isfile('./' + item + '.mp4')) & dl_enabled:
        best.download(filepath='./'+item+'.mp4')
    counter += 1
