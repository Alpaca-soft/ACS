from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
    )

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]
