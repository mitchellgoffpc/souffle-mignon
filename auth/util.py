import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

from django.conf import settings


# OAuth1Session for twitter
class TwitterSession(OAuth1Session):
    def __init__(self, **kwargs):
        super(TwitterSession, self).__init__(
            settings.TWITTER.get('key'),
            client_secret = settings.TWITTER.get('secret'),
            **kwargs)


# Fetch recent tweets
def tweets():
    key = settings.TWITTER.get('key')
    secret = settings.TWITTER.get('secret')
    auth = HTTPBasicAuth(key, secret)
    client = BackendApplicationClient(client_id=key)
    session = OAuth2Session(client=client)
    token = session.fetch_token(token_url="https://api.twitter.com/oauth2/token", auth=auth)

    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = { 'screen_name': 'soufflemignon', 'count': 5 }
    response = session.get(url, params=params)
    return response.json()


# Fetch recent videos
def videos():
    key = settings.GOOGLE.get('key')
    url = "https://www.googleapis.com/youtube/v3/search"
    params = { 'part': 'snippet',
               'channelId': 'UCx60rjk4NvoeP25qP4Y56MA',
               'order': 'date',
               'maxResults': 5,
               'key': key }

    response = requests.get(url, params=params)
    return response.json()
