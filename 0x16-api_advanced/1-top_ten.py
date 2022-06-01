#!/usr/bin/python3
""" fx prints hot posts from a subreddit"""
import requests


def top_ten(subreddit):
    """ print titles 10 hottest posts from a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    conditions = {
        "max": 10
    }
    response = requests.get(url, headers=headers, conditions=conditions,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
