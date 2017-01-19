from django.db import models


class Reader(models.Model):
    facebook_token = models.CharField(max_length=255, blank=True)
    twitter_token = models.CharField(max_length=255, blank=True)
    google_token = models.CharField(max_length=255, blank=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    picture = models.URLField(max_length=255)

    signup_date = models.DateTimeField(auto_now_add=True)
    last_seen_date = models.DateTimeField()
