#!/usr/bin/python3
"""script that list 10 commits (from the
    most recent to oldest) of the repository “rails” by the user “rails”
"""
import sys
import requests


if __name__ == "__main__":
    resp_name = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, resp_name)
    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
