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
    svg = models.TextField()

    def __str__(self):
        return self.title



# Comment class
class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments")
    article = models.ForeignKey(Article, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
    entry = models.TextField()



# Like classes
class Like(models.Model):
    class Meta: abstract = True

    date = models.DateTimeField(auto_now_add=True)

class ArticleLike(Like):
    user = models.ForeignKey(User, related_name="article_likes")
    article = models.ForeignKey(Article, related_name="likes")

class CommentLike(Like):
    user = models.ForeignKey(User, related_name="comment_likes")
    comment = models.ForeignKey(Comment, related_name="likes")
