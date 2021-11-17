"""View Instagram user follower count from Instagram public api"""
import requests


def getfollowedby(url):
    """View Instagram user follower count"""
    link = f'https://www.instagram.com/{url}/?__a=1'
    user = requests.get(link)
    return (user.json()['graphql']['user']['edge_followed_by']['count'])


def getname(url):
    """Split the URL from the username"""

    sp = url.split("instagram.com/")
    print('\n---------> ', sp)

    rep = sp[1].replace("/", "")
    print('\n---------> ', rep)

    return rep
