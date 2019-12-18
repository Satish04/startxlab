# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
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
from .serializers import (UsersSerializer, CommentsSerializer, LikeDislikeSerializer)

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
                return render(request, 'login.html', {'title': 'Page', 'content': 'Hello Login'})
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
                    serializer_class = CommentsSerializer
                    comments = CommentsModel.objects.all().order_by('-created_date')
                    comment_data = serializer_class(comments, many=True).data
                    print comment_data
                    if len(comment_data) > 0:
                        for item in comment_data:
                            item['created_date'] = (datetime.datetime.strptime(item['created_date'], '%Y-%m-%dT%H:%M:%S.%f')).strftime('%d %b, %Y %I:%M %p')
                            condition1 = Q(user_id=item['user_id'])
                            user = Users.objects.filter(condition1)
                            user_detail = UsersSerializer(user, many=True).data
                            item['user_details'] = user_detail[0]

                            condition1 = Q(comment_id=item['comment_id'])
                            condition2 = Q(user_id=users[0]['user_id'])
                            get_likedislike = LikedislikeModel.objects.filter(condition1 & condition2)
                            if get_likedislike:
                                likedislike = LikeDislikeSerializer(get_likedislike, many=True).data
                                item['likedislike'] = likedislike[0]['likedisliked']
                            else:
                                item['likedislike'] = 0

                        return render(request, 'home.html', {'title': 'Page', 'data': comment_data, 'member_id': users[0]['user_id']})
                    return render(request, 'home.html', {'title': 'Page', 'data': False, 'member_id': ''})

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
                if len(comment_data) > 0:
                    for item in comment_data:
                        item['created_date'] = (datetime.datetime.strptime(item['created_date'], '%Y-%m-%dT%H:%M:%S.%f')).strftime('%d %b, %Y %I:%M %p')

                        condition1 = Q(user_id=item['user_id'])
                        user = Users.objects.filter(condition1)
                        user_detail = UsersSerializer(user, many=True).data
                        item['user_details'] = user_detail[0]

                        condition1 = Q(comment_id=item['comment_id'])
                        condition2 = Q(user_id=member_id)
                        get_likedislike = LikedislikeModel.objects.filter(condition1 & condition2)
                        if get_likedislike:
                            likedislike = LikeDislikeSerializer(get_likedislike, many=True).data
                            item['likedislike'] = likedislike[0]['likedisliked']
                        else:
                            item['likedislike'] =  0
                    return HttpResponse(json.dumps(comment_data), content_type="application/json")
                return render(request, 'home.html', {'title': 'Page', 'comments': False, 'member_id': member_id})
        else:
            return render(request, 'login.html', {'title': 'Page', 'content': 'Hello Login'})


class Likedislike(viewsets.ViewSet):
    def likedislike(self, request):
        print request.data
        member_id = request.session.get('member_id', False)
        if member_id:
            comment_id = request.data['commnet_id']
            #user_id = member_id
            print comment_id, 'njihu'
            likedisliked = request.data['likedisliked']
            if comment_id != '' and likedisliked != '':
                data = LikedislikeModel(
                    comment_id=comment_id,
                    user_id=member_id,
                    likedisliked=likedisliked,
                )
                data.save()
                condition1 = Q(comment_id=comment_id)
                condition2 = Q(user_id=member_id)
                get_likedislike = LikedislikeModel.objects.filter(condition1 & condition2)
                likedislike_res = LikeDislikeSerializer(get_likedislike, many=True).data
                return HttpResponse(json.dumps(likedislike_res), content_type="application/json")
        else:
            return render(request, 'login.html', {'title': 'Page', 'content': 'Hello Login'})
        pass
    pass



