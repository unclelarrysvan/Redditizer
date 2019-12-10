import requests
import requests.auth
import os

class Authorizer:
    def __init__(self):
        self.access_token = None
        self.response = None

    def authorize(self):
        client_auth = requests.auth.HTTPBasicAuth(os.environ.get('REDDIT_API_SCRIPT_ID'), os.environ.get('REDDIT_API_SCRIPT_SECRET'))
        post_data = {"grant_type": "password", "username": os.environ.get('REDDIT_USERNAME'), "password": os.environ.get('REDDIT_PASSWORD')}
        headers = {"User-Agent": "ChangeMeClient/0.1 by UncleLarrysVan"}
        self.response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
        self.access_token = self.response.json()['access_token']
