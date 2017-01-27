from django import template

from articles.models import Comment
from articles.models import Article
from articles.models import ArticleLike


register = template.Library()

@register.filter(name='likes')
def likes(user, obj):
    if obj.__class__ is Comment:
        return user in [like.user for like in obj.likes.all()]
    elif obj.__class__ is Article:
        return ArticleLike.objects.filter(
            article=obj,
            user=user).exists()
