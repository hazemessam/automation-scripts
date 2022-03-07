#! /usr/bin/python3

"""
Convert orderd images inside a folder to a pdf file
with the name of the folder.
"""

import os
import img2pdf
from termcolor import colored


files_names = os.listdir() 
imgs_names = [name for name in files_names if name.endswith('.png', '.jpg', '.jpeg')]
imgs_names.sort(key=lambda name:int(name.split('.')[0]))
dir_name = os.path.basename(os.getcwd())
pdf_name = f'{dir_name}.pdf'

with open(pdf_name, 'wb') as pdf:
    pdf.write(img2pdf.convert(imgs_names))
    print(colored(f'{pdf_name} was created', 'green'))
