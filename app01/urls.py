from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url('login/', views.login)
]
