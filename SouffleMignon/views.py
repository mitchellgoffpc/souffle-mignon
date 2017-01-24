from django.views.generic import TemplateView
from django.views.generic.list import ListView

from articles.models import Article


class HomeView(ListView):
    template_name = 'index.html'
    header_class = 'dark'
    queryset = Article.objects.order_by('-date')[:5]

class AboutView(TemplateView):
    template_name = 'about.html'
    header_class = 'dark'
