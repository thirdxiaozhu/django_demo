from django.conf.urls import url
from django.urls import path , re_path
from django.contrib import admin
from student import views

urlpatterns = [
    path('index/',views.index),
    path('showstatu/',views.showstatu),
]