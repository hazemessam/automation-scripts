#!/usr/bin/python3

"""
A simple tool allows you to store (local or web) links
and then you can pop a random link and open it. 
It will help you when you have many links to check 
and you don't know which one you should pick first.
"""

import os
from random import randint
from sys import argv, exit
from termcolor import colored
import webbrowser
from os import system


DB_FILE_PATH = '/home/hazem/data/randlink.db'


class RandLst:
    def __init__(self):
        self.__items = list()

    def push(self, item):
        """Add new item to the list"""
        item = item.strip()
        self.__items.append(item)

    def pop(self):
        """Delete a random item form the list"""
        if len(self.__items) > 0:
            start_idx = 0
            end_idx = len(self.__items) - 1
            rand_idx = randint(start_idx, end_idx)
            return self.__items.pop(rand_idx)
        else: 
            return None

    def list(self):
        return self.__items

    def load(self):
        """Load the existing items from the db file"""
        try:
            if not os.path.exists(DB_FILE_PATH):
                open(DB_FILE_PATH, 'w').close()
            with open(DB_FILE_PATH, 'r') as file:
                for item in file:
                    self.push(item)
        except Exception as e:
            print(colored('Can\'t load items', 'red'))
            print(e)
            exit()
    
    def save(self):
        """Save the items to the db file"""
        with open(DB_FILE_PATH, 'w') as file:
            file.write('\n'.join(self.__items))


def main():
    """
    Check the argument flag 
    if '--add' or '--push' or '-a' add the passed link to the db 
    else if '--get' or '--pop' or '-g' pop a random link then open it
    else if '--list' or '-l' list all links
    """
    is_push_operation = len(argv) == 3 and (argv[1] == '--push' or argv[1] == '--add' or argv[1] == '-a')
    is_pop_operation = len(argv) == 2 and (argv[1] == '--pop' or argv[1] == '--get' or argv[1] == '-g')
    is_list_operation = len(argv) == 2 and  (argv[1] == '--list' or argv[1] == '-l')
    if is_push_operation or is_pop_operation or is_list_operation:
        links = RandLst()
        links.load()
        if is_list_operation:
            print('\n'.join(links.list()))
        elif is_push_operation:
            link = argv[2]
            links.push(link)
            links.save()
            print(colored(f'{link} was added!', 'green'))
        else:
            link = links.pop()
            if link:
                links.save()
                print(colored(f'{link} was deleted!', 'red'))
                open_link = input(f'Open {link} (y or n)? ')
                if open_link.lower() == 'y':
                    if link.startswith('https://'):
                        webbrowser.open(link)
                    else:
                        if ' ' in link:
                            link = f'\"{link}\"'
                        system(f'xdg-open {link}')
            else:
                print(colored('No links!', 'red'))
        
    else:
        print('Usage:\n\trandlink [--push | --add | -a] <link>\t:\tadd a new link\n\trandlink [--pop | --get | -g]\t\t:\tpop a random link then open it\n\trandlink [--list | -l]\t\t\t:\tlist all links')


if __name__ == "__main__":
    main()
