import requests
from models.response import *
from models.link import *

class Subreddit:
    def __init__(self, access_token):
        self.access_token = access_token

    def all_my_subreddit_names(self, names = [], after = ''):
        response = self.my_subreddits(after)

        for sub in response.items:
            names.append(sub['data']['display_name'])

        if response.json()['data']['after']:
            self.all_my_subreddit_names(names, response.json()['data']['after'])

        return names

    def get_subreddit_by_verb(self, sub_name, verb):
        url = "https://oauth.reddit.com/r/" + sub_name + "/" + verb
        return self.get(url)

    def get_subreddit_by_new(self, sub_name):
        return self.get_subreddit_by_verb(sub_name, 'new')

    def downvote(self, post_id):
        url = "https://oauth.reddit.com/api/vote"
        params = { 'dir': '-1', 'id': post_id }

        return requests.post(url, headers=self.headers(), params=params)

    def my_subreddits(self, after):
        subs_url = "https://oauth.reddit.com/subreddits/mine/subscriber"

        if after:
          url = subs_url + "?" + "after=" + after
        else:
          url = subs_url

        return self.get(url)

    def get(self, url):
        return Response(requests.get(url, headers=self.headers()))

    def headers():
        bearer_header = "bearer " + self.access_token
        headers = {"Authorization": bearer_header, "User-Agent": "ChangeMeClient/0.1 by UncleLarrysVan"}
