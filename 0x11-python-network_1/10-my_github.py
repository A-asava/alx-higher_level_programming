#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username
    and password) and uses the GitHub API to display your id
"""
import sys
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    if len(sys.argv) == 3:
        user = sys.argv[1]
        password = sys.argv[2]
        auth = HTTPBasicAuth(user, password)
        req = requests.get('https://api.github.com/user', auth=auth)
        response = req.json()
        print(response.get('id'))
