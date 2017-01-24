from django.db import models

from auth.models import User


# Article class
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=31)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    img = models.URLField(max_length=255)
    entry = models.TextField()

    def __str__(self):
        return self.title



# Comment class
class Comment(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    entry = models.TextField()



# Like classes
class Like(models.Model):
    class Meta: abstract = True

    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

class ArticleLike(Like):
    article = models.ForeignKey(Article)

class CommentLike(Like):
    comment = models.ForeignKey(Comment)
