#!/usr/bin/python3
"""
given username and pw as param, get your id from Github api
usage: ./10-my_github.py [github_username] [github_pw]
"""

import requests
import sys

if _name_ == "_main_":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get('id')
        print(user_id)
    else:
        print(None)
