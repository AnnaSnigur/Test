# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from profile_app import model_choices as mch


class Profile(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField(null=True, blank=True, default=None)
    biography = models.TextField(max_length=500)
    contacts = models.TextField(max_length=200)


class Logger(models.Model):
    path = models.CharField(max_length=128)
    method = models.PositiveIntegerField(choices=mch.METHOD_CHOICES)
    time_delta = models.DecimalField(max_digits=5, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)


class EditProfile(models.Model):
    user = models.PositiveSmallIntegerField()
    ip = models.CharField(max_length=40, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

