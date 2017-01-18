from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from articles.models import Article


class ArticleListView(ListView):
    template_name = "list.html"
    model = Article

class ArticleDetailView(DetailView):
    template_name = "detail.html"
    model = Article
