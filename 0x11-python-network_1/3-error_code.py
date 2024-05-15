#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
    displays the body of the response
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    my_url = sys.argv[1]
    re = urllib.request.Request(my_url)
    try:
        with urllib.request.urlopen(re) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
