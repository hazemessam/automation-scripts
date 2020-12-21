#!/usr/bin/python3
from requests import get
from os import system
from termcolor import colored


surah_num = '1'.zfill(3)
url = f'https://mirrors.quranicaudio.com/tafsir.one/alsidi/{surah_num}.mp3'
res = get(url)

if res.status_code == 200:
    print(colored('success --> 200', 'green'))
    with open(f'{surah_num}.mp3', 'wb') as target:
        target.write(res.content)
    system(f'xdg-open {surah_num}.mp3')
else:
    print(colored(f'failed --> {res.status_code}', 'red'))
