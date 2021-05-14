from django.db import models

# Create your models here.

class UserInfo(models.Model):
    id = models.AutoField(primary_key = True)#创建一个自增的主键字段，
    name = models.CharField(null = False , max_length = 20 , default = "")#创建一个varchar且不能为空
    password = models.CharField(null = False , max_length = 20 , default = "")

class Publisher(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(null = False, max_length = 64 , default = "", unique = True)


class Book(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=64, null = False, unique = True)
    price = models.DecimalField(max_digits = 5 , decimal_places = 2 , default=99.99)
    kucun = models.IntegerField (default = 1000)
    maichu = models.IntegerField (default = 0)

    publisher = models.ForeignKey(to = "Publisher", on_delete = models.CASCADE)

    def __str__(self):
        return "<Book Object: {}>".format(self.title)

class Author(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 16 , null = False , unique = True)
    #告诉ORM，我这张表和Book表是多对多的关系，使得ORM自动生成第三张表（id关联）
    book = models.ManyToManyField(to = "Book" ,through="Author2Book" , through_fields=("author" , "book"))
    #不常用字段使用一对一存储在其他表中
    detail = models.OneToOneField(to="AuthorDetails" , on_delete = models.CASCADE , null = True)

    def __str__(self):
        return "<Author Object: {}>".format(self.name)

class AuthorDetails(models.Model):
    hobby = models.CharField(max_length = 32)
    addr = models.CharField(max_length = 128)


import datetime
class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)
    birthday = models.DateField(default = datetime.date.today)

    def __str__(self):
        return self.name

class Author2Book (models.Model):
    id = models.AutoField(primary_key = True)
#作者ID
    author = models.ForeignKey(to = "Author" , on_delete = models.CASCADE)
#书ID
    book = models.ForeignKey(to = "Book" , on_delete = models.CASCADE)

    class Meta:
        #建立唯一约束 , 无法重复
        unique_together = ("author" ,"book")
