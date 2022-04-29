#!/usr/bin/python3
"""send RQ and display value var"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = argv[1]
    r = get(url)
    print(r.headers.get("X-Request-Id"))
