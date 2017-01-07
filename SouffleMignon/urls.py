from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from home.views import HomeView
from home.views import AboutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^$', HomeView.as_view(), name='home')]
