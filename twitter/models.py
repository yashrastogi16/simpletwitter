# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Tweet(models.Model):
	tweet = models.TextField()
	favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user_favourite')

	def __unicode__(self):
		return self.tweet