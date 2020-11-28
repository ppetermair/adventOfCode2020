#!/usr/bin/env python3

import requests
import sys
import os

day = str(sys.argv[1])
directory = 'day' + day
os.mkdir(directory)

cookie_value = open('cookie').read().replace('\n', '')
cookies = {'session': cookie_value}

print(cookies)

url = 'https://adventofcode.com/2020/day/{}/input'.format(day)
respone = requests.get(url, cookies=cookies)

path = os.path.join(directory, 'input')
open(path, 'wb').write(respone.content)