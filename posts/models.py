# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from  django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    # using predefined User here (django.contrib.auth.models)
    user = models.ForeignKey(User)