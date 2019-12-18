__author__ = 'satish'
import hashlib

from datetime import date, datetime
from rest_framework import serializers


from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'email_id', 'first_name', 'last_name', 'created_date')


    def create(self, validated_data):
        users = Users.objects.create(
            firs_tname=validated_data['firs_tname'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            email_id=validated_data['email'],
            #created_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        )
        return users

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = ('user_id', 'title', 'comment_text', 'comment_id', 'created_date', 'published_date')


class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedislikeModel
        fields = ('id','comment_id', 'user_id', 'created_date', 'likedisliked')

