from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=32, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    entry = models.TextField()

    def __str__(self):
        return self.title
