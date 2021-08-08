#! /usr/bin/python3
"""
Download or get the direct link to download youtube streams as videos or audios.
"""

import pafy
from sys import argv, exit
from termcolor import colored
from os import getenv


def print_streams():
    for id, stream in enumerate(streams, 0):
        stream_size = round(stream.get_filesize() / (1024*1024), 1)
        if str(stream).startswith('normal:'):
            stream_resolution = str(stream.quality).split('x')[-1]
            print(f'{id}) {stream.extension}@{stream_resolution}p -> {stream_size}MB')
        elif str(stream).startswith('audio:'):
            print(f'{id}) {stream.extension}@{stream.quality} -> {stream_size}MB')


if len(argv) != 2 or not argv[1].startswith('https://www.youtube.com'):
    print('Usage:\n\tytb <youtube video link>')
    exit()

link = argv[1]
pfy_obj = pafy.new(url=link)
streams = pfy_obj.streams + pfy_obj.audiostreams

print(f'Title: {pfy_obj.title}')
print('-' * (7 + len(pfy_obj.title)))

while True:
    print_streams()
    
    stream_id = int(input('Choose Stream: '))
    print('-' * (15 + len(str(stream_id))))

    action = int(input('0) Get Direct Link\n1) Download Stream\n2) Choose Another Stream\nChoose Action: '))
    print('-' * (15 + len(str(action))))

    if action not in [0, 1]: continue

    if action == 0: print(colored(streams[stream_id].url, 'green'))
    elif action == 1:
        download_dir = getenv('DOWNLOADS_DIR')
        print(f'Downloading to '+ colored(download_dir, 'green'))
        streams[stream_id].download(filepath=download_dir)
    break
