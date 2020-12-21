#! /usr/bin/python3
import os
from termcolor import colored


files_names = os.listdir() 
imgs_names = [name for name in files_names if name.endswith('.png')]

for name in imgs_names:
    new_name = name.split()[1].replace('(', '').replace(')', '')
    os.rename(name, new_name)
    print(colored(f'{name} was converted to {new_name}', 'green'))
