import requests
import requests.auth
import os

client_auth = requests.auth.HTTPBasicAuth(os.environ.get('REDDIT_API_SCRIPT_ID'), os.environ.get('REDDIT_API_SCRIPT_SECRET'))
post_data = {"grant_type": "password", "username": os.environ.get('REDDIT_USERNAME'), "password": os.environ.get('REDDIT_PASSWORD')}
headers = {"User-Agent": "ChangeMeClient/0.1 by UncleLarrysVan"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
print(response.json())

# headers = {"Authorization": "bearer " + response.json()['access_token'], "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
# print(response.json())

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

sub = Subreddit(response.json()['access_token'])
print(sub.all_subreddit_names())
