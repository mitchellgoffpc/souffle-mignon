from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from .views import HomeView
from .views import AboutView
from .views import SearchView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('auth.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^$', HomeView.as_view(), name='home')]
