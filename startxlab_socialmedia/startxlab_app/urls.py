__author__ = "satish"

from django.conf.urls import url, include
from rest_framework import routers
from views import (User, Comments)

urlpatterns = [

    url(r'user/login/$', User.as_view({'get': 'login'}), name='user_login'),
    url(r'user/signup/$', User.as_view({'get': 'signup'}), name='user_login'),
    url(r'user/home/$', User.as_view({'post': 'home'}),name='user_login'),
    url(r'comments/$', Comments.as_view({'post': 'comments'}),name='user_login')

]