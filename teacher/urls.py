from django.conf.urls import url
from django.urls import path , re_path
from django.contrib import admin
from teacher import views

urlpatterns = [
    path('index/',views.index),
]
