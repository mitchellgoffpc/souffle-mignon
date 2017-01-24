from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    facebook_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    twitter_id = models.CharField(max_length=255, unique=True, blank=True, null=True)

    name = models.CharField(max_length=255)
    picture = models.URLField(max_length=255)
    signup_date = models.DateTimeField(auto_now_add=True)
    last_seen_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
