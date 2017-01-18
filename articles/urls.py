from django.conf.urls import url

from articles.views import ArticleDetailView
from articles.views import ArticleListView


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name="list"),
    url(r'(?P<slug>[A-Za-z0-9_\-]+)/', ArticleDetailView.as_view(), name="detail")]
