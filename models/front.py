import requests

class FrontPage:
    def __init__(self, access_token):
        self.access_token = access_token
        self.url = "https://oauth.reddit.com/best"

    def titles(self):
        for item in self.front_page().json()['data']['children']:
            print('Title: '     + item['data']['title'])
            print('Subreddit: ' + item['data']['subreddit'])

    def front_page(self):
        bearer_header = "bearer " + self.access_token
        headers = {"Authorization": bearer_header, "User-Agent": "ChangeMeClient/0.1 by UncleLarrysVan"}

        return requests.get(self.url, headers=headers)
