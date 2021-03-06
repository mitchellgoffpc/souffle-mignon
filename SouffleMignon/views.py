from django.views.generic import TemplateView
from django.views.generic.list import ListView

import auth.util
from articles.models import Article


class HomeView(ListView):
    template_name = 'index.html'
    header_class = 'dark'
    no_title = True
    queryset = Article.objects.order_by('-date')[:6]

    def tweets(self): return auth.util.tweets()
    def videos(self): return auth.util.videos()['items']

class AboutView(TemplateView):
    template_name = 'about.html'
    header_class = 'dark'

class SearchView(TemplateView):
    template_name = 'search.html'

    def query(self):
        return self.request.GET.get('q', '')
