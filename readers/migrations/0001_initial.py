# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_token', models.CharField(blank=True, max_length=255)),
                ('twitter_token', models.CharField(blank=True, max_length=255)),
                ('google_token', models.CharField(blank=True, max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('picture', models.URLField(max_length=255)),
                ('signup_date', models.DateTimeField(auto_now_add=True)),
                ('last_seen_date', models.DateTimeField()),
            ],
        ),
    ]
