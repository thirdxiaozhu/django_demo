from django.views import View
from django.urls import path
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate
from app01 import models
from student import models as stu_mod
from teacher import models as tea_mod
from adminstrator import models as adm_mod
from django.http import HttpResponseRedirect, JsonResponse


def zoujiaxv(request):
    return HttpResponse('Hello Zoujiaxv!')


def dundun(request):
    return HttpResponse('Hello DunDun!')


def find1_1(request):
    #ret = request.COOKIES.get("is_login",0)
    #一定要写default和盐值
    ret = request.get_signed_cookie("is_login", default="0", salt="zoujiaxv")
    print(ret)
    if ret == "1":
        #表示已经登录
        return render(request, "1_1/1.html")
    else:
        return redirect("/login/")


def register(request):
    error_msg = ""
    if request.method == 'POST':
        new_name = request.POST.get("stu_id", None)
        new_password = request.POST.get("password", None)
        confirm = request.POST.get("confirm-password", None)
        models.UserInfo.objects.create(name=new_name, password=new_password)
        if new_password == confirm:
            return redirect("/login/")
        else:
            error_msg = "密码不一致，请重试！"

    return render(request, "1_1/register.html", {"error": error_msg})


def login(request):
    error_msg = ""
    if request.method == 'POST':
        stu_id = request.POST.get("stu_id", None)
        password = request.POST.get("password", None)
        print(stu_id, password)
        if stu_id and password:
            ret_name = models.UserInfo.objects.filter(name=stu_id).first()
            if ret_name:
                if password == ret_name.password:
                    rep = redirect("/find1_1/")
                    #加盐
                    rep.set_signed_cookie("is_login", "1", salt="zoujiaxv")
                    return rep

                else:
                    error_msg = "账号密码不一致，请重试！"
            else:
                error_msg = "用户不存在"
        else:
            error_msg = "请输入账号及密码"
    return render(request, "1_1/login.html", {"error": error_msg})


def user_list(request):
    ret = models.UserInfo.objects.all()
    return render(request, "1_1/user_list.html", {"user_list": ret})


def del_user(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.UserInfo.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/user_list")
    else:
        return HttpResponse("Wrong!")


def edit_user(request):
    #如果是表单
    if request.method == "POST":
        #print(request.POST)
        #获取网页内name="id"的input框中的值
        edit_id = request.POST.get("id")
        #获取网页内name="edit"的input框中的值,作为即将被更新的用户名
        new_name = request.POST.get("edit")

        #根据id查找sql中的字典
        edited = models.UserInfo.objects.get(id=edit_id)
        #更改用户名
        edited.name = new_name
        #使生效
        edited.save()

        return redirect('/user_list')

    #如果是GET
    edit_id = request.GET.get("id", None)
    if edit_id:
        edit_obj = models.UserInfo.objects.get(id=edit_id)
        #自动在input框中填充待更改的用户名
        return render(request, "1_1/edit_user.html", {"user": edit_obj})

    else:
        return HttpResponse("Wrong!")


def change_password(request):
    error_msg = ""
    if request.method == "POST":
        edit_name = request.POST.get("username")
        new_password = request.POST.get("new_password")

        edited = models.UserInfo.objects.filter(name=edit_name).first()
        if edited:
            edited.password = new_password
            edited.save()
            return redirect("/login")
        else:
            error_msg = "用户不存在"

    return render(request, '1_1/change_password.html', {"error": error_msg})


def book_list(request):
    all_book = models.Book.objects.all()

    return render(request, "1_1/book_list_2.html", {"book_list": all_book})

#FBV


def add_book(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        print(new_title + ' ' + new_publisher_id)
        #创建新书对象
        models.Book.objects.create(
            title=new_title, publisher_id=new_publisher_id)
        #返回书籍列表页
        return redirect("/book_list/")

    ret = models.Publisher.objects.all()
    return render(request, '1_1/add_book.html', {"publisher_list": ret})


#CBV


class AddBook(View):
    def get(self, request):
        ret = models.Publisher.objects.all()
        return render(request, '1_1/add_book.html', {"publisher_list": ret})

    def post(self, request):
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        #print(new_title + ' ' + new_publisher_id)
        #创建新书对象
        models.Book.objects.create(
            title=new_title, publisher_id=new_publisher_id)
        #返回书籍列表页
        return redirect("/book_list/")


def edit_book(request):
    if request.method == "POST":
        #从提交的数据里，提取书名和书关联的出版社
        edit_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_price = request.POST.get("book_price")
        new_kucun = request.POST.get("book_kucun")
        new_maichu = request.POST.get("book_maichu")
        new_publisher_id = request.POST.get("publisher")
        #更新
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title
        edit_book_obj.price = new_price
        edit_book_obj.kucun = new_kucun
        edit_book_obj.maichu = new_maichu
        edit_book_obj.publisher_id = new_publisher_id
        #提交改动
        edit_book_obj.save()
        return redirect('/book_list/')

    edit_id = request.GET.get("id")
    edit_book_obj = models.Book.objects.get(id=edit_id)
#    print(edit_book_obj)

    ret = models.Publisher.objects.all()
    return render(
        request,
        "1_1/edit_book.html",
        {'publisher_list': ret, "book_obj": edit_book_obj}
    )


def author_list(request):
    author_obj = models.Author.objects.get(id=1)
    all_author = models.Author.objects.all().order_by('id')
    return render(request, "1_1/author_list_2.html", {"author_list": all_author})


def delete_author(request, id):
    #author_id = request.GET.get("id")
    author_id = id
    models.Author.objects.get(id=author_id).delete()

    return redirect('/author_list/')


def add_author(request):
    if request.method == "POST":
        new_author = request.POST.get("author_name")
        books = request.POST.getlist("books")  # post提交的是多个数据的时候，用getList

        #创建作者
        new_author_obj = models.Author.objects.create(name=new_author)
        #把新作者和书联系起来
        new_author_obj.book.set(books)
        return HttpResponse("添加新作者成功！")

    all_book = models.Book.objects.all()
    return render(request, "1_1/add_author.html", {"book_list": all_book})


def edit_author(request):
    if request.method == "POST":
        author_id = request.POST.get("author_id")
        new_name = request.POST.get("author_name")
        books = request.POST.getlist("books")
        print(books)

        edit_author_obj = models.Author.objects.get(id=author_id)
        edit_author_obj.name = new_name
        edit_author_obj.book.set(books)
        edit_author_obj.save()

        return redirect("/author_list/")

    edit_id = request.GET.get("id")
    edit_author_obj = models.Author.objects.get(id=edit_id)

    ret = models.Book.objects.all()

    return render(request, "1_1/edit_author.html", {"book_list": ret, "author": edit_author_obj})


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dream(self):
        return "abc"

    def __str__(self):
        return "<Person Object: {}>".format(self.name)


def t_test(request):
    name = "Zou Jiaxv"
    age = 19
    name_list = ['a', 'ab', 'abc']
    name_list_2 = [['a', 'ab', 'abc'], ['c', 'cd', 'cde']]
    name_dict = {"first_name": "Jiaxv", "last_name": "Zou"}

    p1 = Person("ABC", 20)
    p2 = Person("CDE", 25)

    file_size = 123456789

    from datetime import datetime
    now = datetime.now()

    a_html = "<a href='http://www.baidu.com'>这是后端传来的a标签</a>"
    return render(request, "1_1/t_test.html", {
        'name1': name,
        'age1': age,
        'name_list': name_list,
        'name_dict': name_dict,
        'person1': p1,
        'file_size': file_size,
        'now': now,
        'a_html': a_html,
        'name_list_2': name_list_2,
    })


def add_book_1(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        print(new_title + ' ' + new_publisher_id)
        #创建新书对象
        models.Book.objects.create(
            title=new_title, publisher_id=new_publisher_id)
        #返回书籍列表页
        return redirect("/book_list/")

    ret = models.Publisher.objects.all()
    return render(request, '1_1/add_book_1.html', {"publisher_list": ret})


def upload(request):
    if request.method == 'POST':
        #取得上传的文件名
        filename = request.FILES["abc"].name
        #写入文件到服务器
        with open(filename, "wb") as f:
            #chunk——一点一点写入
            for i in request.FILES["abc"].chunks():
                f.write(i)
        return HttpResponse("OK")
    return render(request, "1_1/upload.html")


def json_test(request):
    data = {"name": "小黑", "age": 18}
    #import json
    #data_str = json.dumps(data)
    #return HttpResponse(data_str)

    from django.http import JsonResponse

    return JsonResponse(data)


def test2(request, year, title):
    print(year)
    print(title)
    return HttpResponse("OK")


def test_page(request):
    return render(request, "1_1/test2.html")


def index(request):
    return render(request, "eas/cover.html")


def delete(request, table_name, delete_id):
    print(table_name, delete_id)

#从另外一个文件根据字符串返回具体的变量
    table_name = table_name.capitalize()
    if hasattr(models, table_name):
        #如果能找到
        table_class = getattr(models, table_name)
        try:
            table_class.objects.get(id=delete_id).delete()
        except Exception as e:
            print(str(e))

        table_name = table_name.lower()
        ret_table_title = "/" + table_name + "_list/"
        print(table_name)
        return redirect("{}".format(ret_table_title))
        #return HttpResponse("表名:{} id:{}".format(table_name, delete_id))
    else:
        return HttpResponse("表不存在！")


def start(request):
    return render(request, "1_1/1.html")


def signin(request):
    if request.session.has_key('islogin'):
        usertype = request.session.get('usertype')
        if usertype == "student":
            return redirect('/student/index')
        elif usertype == "teacher":
            return redirect('/teacher/index')
        else:
            return redirect('/admin/index')

    else:
        if 'userid' in request.COOKIES:
            userid = request.get_signed_cookie(
                'userid', default="0", salt="salt")
            password = request.get_signed_cookie(
                'password', default="0", salt="salt")

        else:
            userid = ''
            password = ''

    return render(request, "eas/sign_in.html", {'userid': userid, 'password': password})


def signin_update(request):
    #检查ajax传入信息
    print(request.POST)
    #处理传入字段
    userid = request.POST.get("userid")
    password = request.POST.get("password")
    usertype = request.POST.get("radio")
    is_remember = request.POST.get("remember")

    if usertype == "student":
        dbdata = adm_mod.StudentInfo.objects.filter(
            stu_id=userid, password=password)
        response = JsonResponse({'res': 1, 'usertype': 1})
    elif usertype == "teacher":
        dbdata = adm_mod.TeacherInfo.objects.filter(
            tea_id=userid, password=password)
        response = JsonResponse({'res': 1, 'usertype': 2})
    else:
        dbdata = adm_mod.AdminInfo.objects.filter(
            adm_id=userid, password=password)
        response = JsonResponse({'res': 1, 'usertype': 3})

    #cookie记住账号密码七天
    if is_remember == "on":
        response.set_signed_cookie(
            'userid', userid, salt="salt", max_age=7*24*3600)
        response.set_signed_cookie(
            'password', password, salt="salt", max_age=7*24*3600)
        response.set_signed_cookie(
            'usertype', usertype, salt="salt", max_age=7*24*3600)

    #如果dbdata不为空（在数据库找到对应的id和密码）
    if dbdata:
        request.session['islogin'] = True
        request.session['usertype'] = usertype
        request.session['userid'] = userid
        return response
    #否则只返回一个json字典
    else:
        return JsonResponse({'res': 0})


def home(request):
    return HttpResponse("aaa")


#退出登录
def logout(request):
    rep = redirect("/signin/")
    rep.delete_cookie("userid")
    rep.delete_cookie("password")
    rep.delete_cookie("usertype")
    request.session.flush()
    return rep


def ajax_test(request):
    return render(request, "1_1/ajax_test.html")


def ajax_add(request):
    print(request.GET)
    i1 = request.GET.get("i1")
    i2 = request.GET.get("i2")

    i1 = int(i1)
    i2 = int(i2)
    print(i1, i2)

    ret = i1+i2
    return HttpResponse(ret)


def ajax_img(request):
    #url="http://bigbigcrab.xyz/static/img/20201104224052.png"
    url = "http://baidu.com"
    return HttpResponse(url)


def ajax_add_2(request):
    print(request.POST)
    i1 = request.POST.get("i1")
    i2 = request.POST.get("i2")

    i1 = int(i1)
    i2 = int(i2)
    print(i1, i2)

    ret = i1+i2
    return HttpResponse(ret)
