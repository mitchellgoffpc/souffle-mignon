from django.conf.urls import url

from .views import TwitterAuthView
from .views import FacebookAuthView


urlpatterns = [
    url(r'^twitter/', TwitterAuthView.as_view()),
    url(r'^facebook/', FacebookAuthView.as_view())]
