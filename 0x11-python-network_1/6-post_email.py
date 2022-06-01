#!/usr/bin/python3
"""sends a POST RQ and diplsay body"""
from sys import argv
from requests import post


if __name__ == "__main__":
    value = {"email": argv[2]}
    request = post(argv[1], data=value)
    print(request.text)
