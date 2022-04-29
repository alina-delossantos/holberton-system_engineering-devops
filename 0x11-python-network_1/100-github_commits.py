#!/usr/bin/python3
"""list 10 latters commits"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos"
    url += "/{}/{}/commits".format(argv[2], argv[1])
    request = get(url)
    commits = request.json()
    try:
        for i in range(10):
            print(commits.get('sha'), end=': ')
            print(commits.get('commit').get('author').get('name'))
    except IndexError:
        pass
