# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tweet

# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'tweet')

admin.site.register(Tweet, TweetAdmin)
