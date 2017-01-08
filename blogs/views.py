from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blogs.models import Blog


class BlogListView(ListView):
    template_name = "list.html"
    model = Blog

class BlogDetailView(DetailView):
    template_name = "detail.html"
    model = Blog
