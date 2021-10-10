#!/usr/bin/env python
# This scripts uses the libraries published here:
# https://github.com/hzeller/rpi-rgb-led-matrix
# Modified https://gist.github.com/chubbyemu/4ca0c68878c6d978d067da4a36bcc71d
# license           : MIT
# py version        : 2.7
# author            : @g0vandS, Govand Sinjari


# Display news from RSS feeds on LED Matrix

import os, time, threading, random
import feedparser
from PIL import Image, ImageFont, ImageDraw
from random import shuffle

BITLY_ACCESS_TOKEN="BITLY_ACCESS_TOKEN"

items=[]

feeds=[
    #enter all news feeds you want here
"http://feeds.bbci.co.uk/news/world/rss.xml"
    ]

def populateItems():
    #first clear out everything
    del items[:]

    for url in feeds:
        feed=feedparser.parse(url)
        posts=feed["items"]
        for post in posts:
            items.append(str(post.title.replace("'", "‘").replace("(", "").replace(")", "")))
    shuffle(items)
    print(len(items))
    print(items)


def run():
    print("News Fetched at {}\n".format(time.ctime()))
    populateItems()
    threading.Timer(len(items) * 60, run).start()
    showOnLEDDisplay()

def showOnLEDDisplay():
    for disp in items:
        os.system('sudo ./scrolling-text-example -y -2 -C "14,107,14" --led-rows=16 --led-cols=32 --led-chain=6 --led-slowdown-gpio=2 -f ../fonts/10x20.bdf -l 1 -s 10 '+disp)

if __name__ == '__main__':
    run()
