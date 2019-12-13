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

    def my_subreddits(self, after):
        url = "https://oauth.reddit.com/subreddits/mine/subscriber"
        params = { 'after': after }

        return self.get(url, params)

    def get_subreddit_by_verb(self, sub_name, verb):
        url = "https://oauth.reddit.com/r/" + sub_name + "/" + verb
        return self.get(url)

    def get_subreddit_by_new(self, sub_name):
        return self.get_subreddit_by_verb(sub_name, 'new')

    def downvote(self, post_id):
        return self.vote(post_id, '-1')

    def upvote(self, post_id):
        return self.vote(post_id, '1')

    def vote(self, post_id, direction):
        url = "https://oauth.reddit.com/api/vote"
        params = { 'dir': direction, 'id': post_id }

        return requests.post(url, headers=self.auth_headers(), params=params)

    def get(self, url, params = {}):
        return Response(
                   requests.get(url, headers=self.auth_headers(), params=params)
               )

    def auth_headers(self):
        bearer_header = "bearer " + self.access_token
        return {"Authorization": bearer_header, "User-Agent": "ChangeMeClient/0.1 by UncleLarrysVan"}
