#!/usr/bin/python3
"""
Display the times of the muslims prayers and 
the remaining time until the next prayer in the day.
"""

from datetime import date, datetime
import requests
from termcolor import colored
from sys import exit


class Prayer:
    names = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']

    def __init__(self, name, time_24):
        self.name = name
        self.time_24 = time_24
        self.time_12 = None

    def format(self):
        self.time_12 = datetime.strptime(self.time_24, '%H:%M').strftime('%I:%M %P')

    def is_upcoming(self):
        current_time_obj = datetime.now().time()
        prayer_time_obj = datetime.strptime(self.time_24, '%H:%M').time()
        if prayer_time_obj >= current_time_obj:
            return True
        return False

    def remaining_time(self):
        current_time_str = datetime.now().strftime('%H:%M')   
        current_time_obj = datetime.strptime(current_time_str , '%H:%M')
        prayer_time_obj = datetime.strptime(self.time_24, '%H:%M')
        remaining_time = prayer_time_obj - current_time_obj
        return ':'.join(str(remaining_time).split(':')[:-1])

    def __repr__(self):
        return f'{self.name}\t ->  {self.time_12}'


# Get current year, month and day
current_year = date.today().year
current_month = date.today().month
current_day = date.today().day

# Create the API endpoint URL and fetch the API
api_base_url = 'http://api.aladhan.com/v1/calendarByCity' 
api_url = f'{api_base_url}?city=damietta&country=egypt&method=5&month={current_month}&year={current_year}'
res = None
try:
    res = requests.get(api_url)
except:
    print(colored('Request failed!', 'red'))
    exit()

# Parse the respone to get prayer times
if res.status_code == 200:
    data = res.json()['data']
    current_day_data = data[current_day - 1]
    
    next_prayer_found = False
    for prayer_name in Prayer.names:
        prayer_time_24 = current_day_data['timings'][prayer_name].split()[0]
        prayer = Prayer(
            name=prayer_name, 
            time_24=prayer_time_24
        )
        prayer.format()
        
        if not next_prayer_found and prayer.is_upcoming():
            print(colored(f'{prayer}  ->  ({prayer.remaining_time()})', 'green'))
            next_prayer_found = True
        else:
            print(prayer)
else:
    print(colored(f'Request failed --> {res.status_code}', 'red'))
