#!/usr/bin/python3
"""Print the top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the top 10 hot posts of a subreddit."""
    base_url = "https://www.reddit.com"
    headers = {
        "User-Agent": "ALXProjectBot:Devops_0x16 v1.0.0 Advanced API",
    }
    resp = requests.get(
        "{}/r/{}/hot.json".format(base_url, subreddit),
        headers=headers,
        allow_redirects=False,
        params={
            "limit": 10
        }
    )
    if resp.status_code != 200:
        print("None")
        return

    posts = resp.json().get("data", {}).get("children")

    if posts is None:
        print("None")
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
