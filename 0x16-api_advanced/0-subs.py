#!usr/bin/python3
"""
a function that queries a subreddit and returns no of subs
"""

import requests


def number_of_subscribers(subreddit):
    """queries a subreddit and returns no of subs"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
