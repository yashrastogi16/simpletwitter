# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + ((_('Twitter'), {'fields': ('tweet', 'follower')}), )

# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
