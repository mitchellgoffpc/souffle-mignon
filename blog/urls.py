from django.conf.urls import url
from django.views.generic import View

urlpatterns = [
    url(r'^$', View.as_view())]
