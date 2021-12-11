""" Add metadata to the Quran mp3 files """

import os
from sys import argv
import eyed3
from eyed3.id3.frames import ImageFrame


def attatch_tags(filepath):
    IMG_PATH = '/mnt/d/Media/Pictures/Islamic/Quran.jpg'
    IMG_TYPE = 'image/jpeg'
    
    filename = os.path.basename(filepath)
    track_num, title, artist = filename.split('.')[0].split(' - ')
    print(f'Path: {filepath}', f'Title: {title}', f'Artist: {artist}', f'#: {track_num}', sep='\n')

    audiofile = eyed3.load(filepath)

    if audiofile.tag.title is None: audiofile.tag.title = title
    if audiofile.tag.artist is None: audiofile.tag.artist = artist
    if audiofile.tag.genre is None: audiofile.tag.genre = 'Quran'
    if audiofile.tag.album is None: audiofile.tag.album = 'Quran'
    if audiofile.tag.track_num is None: audiofile.tag.track_num = track_num
    if len(audiofile.tag.images) == 0:
        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(IMG_PATH, 'rb').read(), IMG_TYPE)

    audiofile.tag.save()


def main():
    path = argv[1]
    
    if os.path.exists(path):
        if os.path.isfile(path):
            attatch_tags(filepath=path)
        else:
            os.chdir(path)
            for filename in os.listdir():
                attatch_tags(filename)
    else: 
        print(f'{path} not exist!')


main()
