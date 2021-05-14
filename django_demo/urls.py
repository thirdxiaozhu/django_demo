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
from django.urls import path , include , re_path
from app01 import views
from app01 import urls as app01_urls
from student import urls as student_urls
from adminstrator import urls as admin_urls
from teacher import urls as teacher_urls
from chat import urls as chat_urls
#from app02 import urls as app02_urls


urlpatterns = [
    path('zoujiaxv/', views.zoujiaxv),
    path('dundun/', views.dundun),
    path('find1_1/',views.find1_1),
    path('login/',views.login),
    path('register/',views.register),
    path('user_list/',views.user_list),
    path('del_user/',views.del_user),
    path('edit_user/',views.edit_user),
    path('change_password/',views.change_password),
    path('book_list/',views.book_list),
    #path('add_book/',views.add_book),
    path('add_book/',views.AddBook.as_view()),
    path('edit_book/',views.edit_book),
    path('author_list/',views.author_list),
    path('delete_author/<int:id>',views.delete_author , name="dela"),
    path('add_author/',views.add_author),
    path('edit_author/',views.edit_author),
    path('t_test/',views.t_test),
    path('add_book_1/',views.add_book_1),
    path('upload/',views.upload),
    path('json_test/',views.json_test , name="json"),
    path('app01/',include(app01_urls)),
    path('test_page/',views.test_page),
    path('test2/<int:year>/<str:title>',views.test2 , name="newtest"),
    path('delete/<str:table_name>/<int:delete_id>',views.delete, name="delete"),
    path('',views.index),
    path('start/',views.start),
    path('student/',include(student_urls) , name="student"),
    path('admin/',include(admin_urls) , name="admin"),
    path('teacher/',include(teacher_urls) , name="teacher"),
    path('chat/',include(chat_urls) , name="chat"),
    path('signin/',views.signin, name="signin"),
    path('signin_update/',views.signin_update),
    path('home/',views.home),
    path('logout/',views.logout),
    path('ajax_add/',views.ajax_add),
    path('ajax_add_2/',views.ajax_add_2),
    path('ajax_test/',views.ajax_test),
    path('ajax_img/', views.ajax_img),
]
