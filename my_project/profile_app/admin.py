# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from profile_app.models import Profile


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = ['username',
              'first_name',
              'last_name',
              'is_active',
              'birth_date',
              'biography',
              'contacts']


admin.site.register(Profile, UserAdmin)
