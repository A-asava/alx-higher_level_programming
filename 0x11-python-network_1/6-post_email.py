#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends
    a POST request to the passed URL
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    req = requests.post(url, email)
    print(req.text)
