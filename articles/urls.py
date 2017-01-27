from django.conf.urls import url

from articles.views import ArticleDetailView
from articles.views import ArticleListView
from articles.views import LikeView
from articles.views import CommentView


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name="list"),
    url(r'like/', LikeView.as_view(), name="likes"),
    url(r'comment/', CommentView.as_view(), name="comments"),
    url(r'(?P<slug>[A-Za-z0-9_\-]+)/', ArticleDetailView.as_view(), name="detail")]
