# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import hashlib

# Create your views here.
__authon__ = "satish"

import json
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from django.db.models import Q

from .models import *
from .serializers import (UsersSerializer, CommentsSerializer)

class User(viewsets.ViewSet):
    def login(self,request):
        return render(request, 'login.html', {'title': 'Page',  'content': 'Hello Login'})


    def signup(self, request):
        return render(request, 'signup.html', {'title': 'Page', 'content': 'Hello Login'})

    def home(self, request):
        print request.data
        serializer_class = UsersSerializer
        if request.method == 'POST':
            if request.data['from_type'] == 'signup':
                data = Users(
                first_name = request.data['fname'],
                last_name = request.data['lname'],
                email_id = request.data['email'],
                password = hashlib.md5(request.data['pass'].encode('utf8')).hexdigest() #hashlib.md5(p.encode('utf8')).hexdigest()
                )
                data.save()

            else:

                email = request.data['username']
                password = hashlib.md5(request.data['pass'].encode('utf8')).hexdigest()
                condition1 = Q(email_id=email)
                condition2 = Q(password=password)

                user_data = Users.objects.filter(condition1 & condition2 )
                users = serializer_class(user_data, many=True).data
                if len(users) == 0:
                    return render(request, 'login.html', {'title': 'Page', 'content': 'Hello Login'})
                else:
                    request.session['member_id'] = users[0]['user_id']
            return render(request, 'home.html', {'title': 'Page', 'data': users, 'member_id': users[0]['user_id']})

class Comments(viewsets.ViewSet):
    def comments(self, request):
        member_id = request.session.get('member_id', False)
        if member_id:
            comment = request.data['post_data']
            title = request.data['title']
            if comment != '' and title != '':
                data = CommentsModel(
                    comment_text = comment,
                    user_id = member_id,
                    title = title,
                )
                data.save()
                serializer_class = CommentsSerializer
                comments = CommentsModel.objects.all().order_by('-created_date')
                comment_data = serializer_class(comments, many=True).data
                for item in comment_data:
                    condition1 = Q(user_id=item['user_id'])
                    user = Users.objects.filter(condition1)
                    user_detail = UsersSerializer(user, many=True).data
                    item['user_details'] = user_detail[0]
            return render(request, 'home.html', {'title': 'Page', 'comments': comment_data, 'member_id': member_id})
        else:
            return render(request, 'login.html', {'title': 'Page', 'content': 'Hello Login'})



