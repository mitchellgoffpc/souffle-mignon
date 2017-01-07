from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)
    entry = models.TextField()
