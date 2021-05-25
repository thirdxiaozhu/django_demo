"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from adminstrator import views
#from app02 import urls as app02_urls


urlpatterns = [
    path('test/', views.test),
    path('index/', views.index),
    path('status/', views.status),
    path('teacherlist/', views.teacherlist),
    path('courselist/', views.courselist),
    path('getareas/', views.getAreas),
    path('getCountry/', views.getCountry),
    path('getProvince/', views.getProvince),
    path('getCity/', views.getCity),
    path('getCollege/', views.getCollege),
    path('getCollege4tc/', views.getCollege4tc),
    path('getTeacherCollege/', views.getTeacherCollege),
    path('getMajor/', views.getMajor),
    path('getClass/', views.getClass),
    path('showstudents/', views.showstudents),
    path('edit_student/', views.edit_student),
    path('edit_teacher/', views.edit_teacher),
    path('edit_course/', views.edit_course),
    path('judgename/', views.judgename),
    path('delete_student/', views.delete_student),
    path('delete_teacher/', views.delete_teacher),
    path('add_student/', views.add_student),
    path('add_teacher/', views.add_teacher),
    path('add_course/', views.add_course),
    path('searchstatu/', views.searchstatu),
    path('searchroom/', views.searchroom),
    path('searchcourse/', views.searchcourse),
    path('classrooms/',views.classrooms),
    path('edit_classroom/',views.edit_classroom),
    path('getFunction/', views.getFunction),
    path('getBuilding/', views.getBuilding),
    path('getroomlist/', views.getroomlist),
    path('getcourse/', views.getcourse),
    path('getteacher/', views.getteacher),
    path('getselcourse/', views.getselcourse),
    path('getteacou/', views.getteacou),
    path('receivebox/', views.receivebox),
    path('filremessage/', views.filremessage, name="fil"),
    path('institute/', views.institute),
]
