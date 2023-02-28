#!/usr/bin/python3
"""Print the hot posts of a subreddit."""
import requests
from pprint import pprint


def recurse(subreddit, hot_list=[], after=""):
    """Print the hot posts of a subreddit."""
    base_url = "https://www.reddit.com"
    headers = {
        "User-Agent": "ALXProjectBot:Devops_0x16 v1.0.0 Advanced API",
    }
    resp = requests.get(
        "{}/r/{}/hot.json".format(base_url, subreddit),
        headers=headers,
        allow_redirects=False,
        params={
            "after": after,
        },
    )

    if resp.status_code != 200:
        return hot_list

    posts = resp.json().get("data", {})

    after = posts.get("after")

    posts = posts.get("children")

    if len(posts) == 0 or posts is None:
        return hot_list

    posts = [post.get("data", {}).get("title") for post in posts]

    hot_list.extend(posts)

    if after is None:
        return hot_list

    return recurse(subreddit,
                   hot_list,
                   after)
