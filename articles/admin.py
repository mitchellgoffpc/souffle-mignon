from django.contrib import admin

from articles.models import Article
from articles.models import Comment
from articles.models import ArticleLike
from articles.models import CommentLike


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ArticleLike)
admin.site.register(CommentLike)
