from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic.list import ListView

from articles.models import Article


class HomeView(ListView):
    template_name = 'index.html'
    header_class = 'dark'
    queryset = Article.objects.order_by('-date')[:5]


class AboutView(TemplateView):
    template_name = 'about.html'
    header_class = 'dark'


class TwitterLoginView(View):
    def get(self, request, **kwargs):
        key = "J6WHuaYyxsmS8AxfblcyJ1xGk"
        secret = "daGGZ9sF8uFGAZOIjATWomJDnBpN6SM65CFcPnZb7xVJyJ8CBg"
        url = "https://api.twitter.com/oauth/request_token"
        callback = request.GET['callback']
        twitter = OAuth2Session(client_id, redirect_uri=redirect_uri)

        return HttpResponseRedirect(
            "https://api.twitter.com/oauth/authenticate?oauth_token={}"
            .format(twitter.token))
