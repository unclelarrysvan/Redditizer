from models.auth import *
from models.front import *
from models.subreddit import *

auth = Authorizer()
auth.authorize()
print(auth.access_token)

# headers = {"Authorization": "bearer " + response.json()['access_token'], "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
# print(response.json())

front = FrontPage(auth.access_token)

sub = Subreddit(auth.access_token)
#print(sub.all_my_subreddit_names())
