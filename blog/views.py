from django.views.generic import TemplateView

class ListView(TemplateView):
    template_name = "list.html"

class BlogView(TemplateView):
    template_name = "blog.html"
