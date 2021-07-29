#! /usr/bin/python3
"""
Get direct link or download youtube streams (videos & audio).
"""

import pafy
from sys import argv
from termcolor import colored
from os import getenv


link = argv[1]
pfy_obj = pafy.new(url=link)
streams = []
id = 0

print(f'Title: {pfy_obj.title}')
print('-' * (7 + len(pfy_obj.title)))

for stream in pfy_obj.streams:
    streams.append(stream)
    stream_resolution = str(stream.quality).split('x')[-1]
    stream_size = round(stream.get_filesize() / (1024*1024), 1)
    print(f'{id}) {stream.extension}@{stream_resolution}p -> {stream_size}MB')
    id += 1

for stream in pfy_obj.audiostreams:
    streams.append(stream)
    stream_size = round(stream.get_filesize() / (1024*1024), 1)
    print(f'{id}) {stream.extension}@{stream.quality} -> {stream_size}MB')
    id += 1

stream_id = int(input('Choose Stream: '))
print('-' * (15 + len(str(id))))

action = int(input('0) Get Link\n1) Download\nChoose Action: '))
print('-' * (15 + len(str(action))))

if action == 0: print(colored(streams[stream_id].url, 'green'))
elif action == 1: 
    download_dir = getenv('DOWNLOADS_DIR')
    print(f'Downloading to '+ colored(download_dir, 'green'))
    streams[stream_id].download(filepath=download_dir)
