from django.views.generic import TemplateView
from django.views.generic.list import ListView

from blogs.models import Blog


class HomeView(ListView):
    template_name = 'index.html'
    header_class = 'dark'
    model = Blog

class AboutView(TemplateView):
    template_name = 'about.html'
    header_class = 'dark'
