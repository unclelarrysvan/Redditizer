import requests

class Subreddit:
    def __init__(self, access_token):
        self.access_token = access_token

    def all_subreddit_names(self, names = [], after = ''):
        response = self.subreddits(after)

        for sub in response.json()['data']['children']:
            names.append(sub['data']['display_name'])

        if response.json()['data']['after']:
            self.all_subreddit_names(names, response.json()['data']['after'])

        return names

    def subreddits(self, after):
        subs_url = "https://oauth.reddit.com/subreddits/mine/subscriber"

        if after:
          url = subs_url + "?" + "after=" + after
        else:
          url = subs_url

        return self.get(url)

    def get(self, url):
        bearer_header = "bearer " + self.access_token
        headers = {"Authorization": bearer_header, "User-Agent": "ChangeMeClient/0.1 by UncleLarrysVan"}

        return requests.get(url, headers=headers)
