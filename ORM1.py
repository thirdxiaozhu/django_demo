"""
如何在一个Python脚本或文件中，加载Django项目的配置和变量信息
"""

import os
from django.utils import timezone

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
    import django
    django.setup()


print(timezone.now())
"""
#    from app01 import models
    from adminstrator import models
    from django.db.models import Avg,Sum,Max,Min,Count
    from django.db.models import F

    ret = models.ClassRoom.objects.filter(id__gt=16 , id__lt=25)
    for i in ret:
        i.function_id = 1
        i.save()
    print(ret)
    import json
    #属性名一定用双引号!!!!
    s = '{"name" : "zoujiaxv" , "age" : 18}'
    #字符串反序列化成json
    ret = json.loads(s)
    print(ret , type(ret))

    #字典序列化成python中的字符串
    ret2 = json.dumps(ret)
    print(ret2 , type(ret2))

#    models.Book.objects.update(maichu = F("maichu") * 3)

    models.AreaInfo.objects.create(aid='1',atitle='陕西省',aParent='0')
    models.AreaInfo.objects.create(aid='2', atitle='山西省',aParent='0')
    models.AreaInfo.objects.create(aid='101', atitle='渭南市',aParent='1')
    models.AreaInfo.objects.create(aid='102', atitle='宝鸡市', aParent='1')
    models.AreaInfo.objects.create(aid='201', atitle='吕梁市', aParent='2')
    models.AreaInfo.objects.create(aid='202', atitle='忻州市', aParent='2')
    models.AreaInfo.objects.create(aid='10101', atitle='渭南1', aParent='101')
    models.AreaInfo.objects.create(aid='10102', atitle='渭南2', aParent='101')
    models.AreaInfo.objects.create(aid='10201', atitle='宝鸡1', aParent='102')
    models.AreaInfo.objects.create(aid='10202', atitle='宝鸡2', aParent='102')
    models.AreaInfo.objects.create(aid='20101', atitle='吕梁1', aParent='201')
    models.AreaInfo.objects.create(aid='20102', atitle='吕梁2', aParent='201')
    models.AreaInfo.objects.create(aid='20201', atitle='忻州1', aParent='202')
    models.AreaInfo.objects.create(aid='20202', atitle='忻州2', aParent='202')


    ret = models.Book.objects.filter(kucun__gt = F("maichu"))
    print(ret)

    
    #查询每个作者出的书的总价格
    ret = models.Author.objects.all().annotate(price_sum = Sum("book__price")).values_list("name" , "price_sum")
    print(ret)

#查询作者数量大于1的书
    ret = models.Book.objects.all().annotate(author_num = Count("author")).filter(author_num__gt=1)
    print(ret)

    for book in ret:
        print("书名：{}， 作者数量：{}".format(book.title , book.author_num))
#    列出每一本书的作者个数

    ret = models.Book.objects.all().annotate(author_num = Count("author"))

    for book in ret:
        print("书名：{}， 作者数量：{}".format(book.title , book.author_num))


    ret = models.Book.objects.all().aggregate(Avg("price"))
    print(ret)

    ret = models.Book.objects.all().aggregate(price_avg = Avg("price") , price_max = Max("price") , price_sum = Sum("price"))
    print(ret)


#多对多
    author_obj = models.Author.objects.first()
    print(author_obj.name)
#展示作者的所有书籍
    ret = author_obj.book.all()
    print(ret)

    author_obj.book.add(29)

#外键查询操作

    #正向查询
    book_obj = models.Book.objects.all().first()
    ret = book_obj.publisher

    print(ret.name)

#双下划线表示跨了一张表
    ret = models.Book.objects.filter(id=1).values("publisher__name")
    print(ret)

#1.基于对象的反向查询
    publisher_obj = models.Publisher.objects.first()
    ret = publisher_obj.book_set.all()
    print(ret)

#2.下划线反向查询
    ret = models.Publisher.objects.filter(id=1).values("book__title")
    print(ret)
    #双下划线查询

    #查询id>1且<4的结果
    ret = models.Person.objects.filter(id__gt=1 , id__lt=4)
    print(ret)
    
    #in查询
    ret = models.Person.objects.filter(id__in=[1,3,5])
    print(ret)

    #exclude和in查询
    ret = models.Person.objects.exclude(id__in=[1,3,5])
    print(ret)

    #contains 字段包含
    ret = models.Person.objects.filter(name__contains="邹")
    print(ret)

    #range查询
    ret = models.Person.objects.filter(id__range=[1,3])
    print(ret)

    print("all".center(30,'*'))
    #查询全部
    ret = models.Person.objects.all()
    print(ret)

    print("get".center(30,'*'))
    #get查询 如果数据不存在会报错！不安全
    ret = models.Person.objects.get(id = 1)
    print(ret)

    print("filter".center(30,'*'))
    #filter 返回的是QuerySet 是个列表，如果想要取出数据需要使用索引
    ret = models.Person.objects.filter(id = 1)
    print("未使用索引:")
    print(ret)
    ret = models.Person.objects.filter(id=1)[0]
    print("使用索引:")
    print(ret)

    print("exclude".center(30,'*'))
    #exclude
    ret = models.Person.objects.exclude(id = 1)
    print(ret)

    print("values".center(30,'*'))
    #values查询某一列所有值 , 为字典
    ret = models.Person.objects.values('birthday')
    print(ret)

    print("values_list".center(30,'*'))
    #values_list查询某一列所有值 , 为元组
    ret = models.Person.objects.values_list('birthday')
    print(ret)

    print("order_by".center(30,'*'))
    #order_by 按照字段排序
    ret = models.Person.objects.all().order_by('birthday')
    print(ret)

    print("reverse".center(30,'*'))
    #reverse 反转排序
    ret = models.Person.objects.all().order_by('birthday').reverse()
    print(ret)

    print("count".center(30,'*'))
    #count 返回数量
    ret = models.Person.objects.all().count()
    print(ret)

    print("first".center(30,'*'))
    #first 
    ret = models.Person.objects.all().first()
    print(ret)

    print("last".center(30,'*'))
    #last
    ret = models.Person.objects.all().last()
    print(ret)

    print("exists".center(30,'*'))
    #exist判断表内是否有信息
    ret = models.Person.objects.exists()
    print(ret)
"""

