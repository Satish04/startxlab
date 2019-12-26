# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_enumfield import enum

__author__ = "satish"
# Create your models here.
from django.db import models


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email_id = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'


class CommentsModel(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_id = models.AutoField(primary_key=True)
    user_id =  models.IntegerField()
    title = models.CharField(max_length=200)
    comment_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'comments'


class Enumlikedislike(enum.Enum):
    like = 1
    dislike = 0
    __default__ = dislike

class LikedislikeModel(models.Model):
    id = models.AutoField(primary_key=True)
    comment_id = models.IntegerField()
    user_id = models.IntegerField()
    likedisliked = enum.EnumField(Enumlikedislike, default=Enumlikedislike.dislike)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'likedislike'
