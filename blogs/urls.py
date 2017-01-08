from django.conf.urls import url

from blogs.views import BlogDetailView
from blogs.views import BlogListView

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name="list"),
    url(r'(?P<slug>[A-Za-z0-9_\-]+)/', BlogDetailView.as_view(), name="detail")]
