from requests_oauthlib import OAuth1Session
from django.conf import settings


# OAuth1Session for twitter
class TwitterSession(OAuth1Session):
    def __init__(self, **kwargs):
        super(TwitterSession, self).__init__(
            settings.TWITTER.get('key'),
            client_secret = settings.TWITTER.get('secret'),
            **kwargs)
