#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter
"""
import urllib.request
import sys


if __name__ == "__main__":
    my_url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    re = urllib.request.Request(my_url, data)
    with urllib.request.urlopen(re) as response:
        print(response.read().decode('utf8'))
