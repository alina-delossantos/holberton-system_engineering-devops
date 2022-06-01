#!/usr/bin/python3
"""takes in a URL amd display value variable of the response"""
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
