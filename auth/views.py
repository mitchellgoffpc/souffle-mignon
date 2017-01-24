import facebook

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic import View

from auth.util import TwitterSession


class TwitterAuthView(View):
    def get(self, request, **kwargs):
        if 'auth' not in request.GET:
            return self.get_request_token(request)
        elif 'oauth_token' in request.GET:
            return self.get_access_token(request)
        else:
            return HttpResponseRedirect(request.GET.get('callback', '/'))

    # First, get a request token from Twitter and redirect the user to
    # Twitter's sign in page
    def get_request_token(self, request):
        oauth = TwitterSession(callback_uri=request.build_absolute_uri() + '&auth=true')
        oauth.fetch_request_token("https://api.twitter.com/oauth/request_token")
        url = oauth.authorization_url("https://api.twitter.com/oauth/authenticate")
        return HttpResponseRedirect(url)

    # Once the user has been authenticated through Twitter, we pull their
    # Twitter profile and use it to log them in
    def get_access_token(self, request):
        oauth = TwitterSession()
        data = oauth.parse_authorization_response(request.build_absolute_uri())
        response = oauth.fetch_access_token('https://api.twitter.com/oauth/access_token')
        profile = oauth.get("https://api.twitter.com/1.1/account/verify_credentials.json")
        user = authenticate(twitter=profile.json())
        login(request, user)

        return HttpResponseRedirect(data.get('callback', '/'))



class FacebookAuthView(View):
    def get(self, request, **kwargs):
        graph = facebook.GraphAPI(access_token=request.GET.get('access_token'))
        profile = graph.get_object(id='me', fields='id,name,picture')
        user = authenticate(facebook=profile)
        login(request, user)

        return HttpResponseRedirect(request.GET.get('callback', '/'))
