from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'
    header_class = 'dark'

class AboutView(TemplateView):
    template_name = 'about.html'
    header_class = 'dark'
