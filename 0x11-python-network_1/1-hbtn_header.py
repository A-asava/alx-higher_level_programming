#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
"""
import urllib.request
import sys


if __name__ == "__main__":
    my_url = sys.argv[1]
    re = urllib.request.Request(my_url)
    with urllib.request.urlopen(re) as response:
        print(response.headers.get('X-Request-Id'))
