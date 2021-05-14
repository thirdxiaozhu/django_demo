from django.db.models.fields import IntegerField
from django.shortcuts import render, HttpResponse, redirect
from django.urls import path
from django.contrib.auth import authenticate
from adminstrator import models
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
import json
import datetime

# Create your views here.


def test(request):
    return render(request, 'eas/test.html')


def getAreas(request):
    return render(request, 'eas/getAreas.html')
#获得国家


def getCountry(request):
    countries = models.Countries.objects.all()
    res = []
    for i in countries:
        res.append([i.aid, i.atitle])
    return JsonResponse({'countries': res})


#获得省份
def getProvince(request):
    country_id = request.GET.get('country_id')
    provinces = models.Provinces.objects.filter(Country=country_id)
    res = []
    for i in provinces:
        res.append([i.aid, i.atitle])
    return JsonResponse({'provinces': res})

#获得城市


def getCity(request):
    province_id = request.GET.get('province_id')
    cities = models.Cities.objects.filter(Province=province_id)
    res = []
    for i in cities:
        res.append([i.aid, i.atitle])
    return JsonResponse({'cities': res})


def index(request):
    return render(request, "eas/admin/admin_index.html")


def status(request):
    return render(request, "eas/admin/admin_status.html", {"student": 1})


def getCollege(request):
    colleges = models.CollegeInfo.objects.all()
    res = []
    for i in colleges:
        res.append([i.id, i.name])
    return JsonResponse({'colleges': res})


def getCollege4tc(request):
    colleges = models.CollegeInfo4tc.objects.all()
    res = []
    for i in colleges:
        res.append([i.id, i.name])
    return JsonResponse({'colleges': res})


def getTeacherCollege(request):
    colleges = models.CollegeInfo4tc.objects.all()
    res = []
    for i in colleges:
        res.append([i.id, i.name])
    return JsonResponse({'colleges': res})


def getMajor(request):
    collegeid = request.GET.get('college_id')
    majors = models.MajorInfo.objects.filter(college_id=collegeid)
    res = []
    for i in majors:
        res.append([i.id, i.name])
    return JsonResponse({'majors': res})


def getClass(request):
    majorid = request.GET.get('major_id')
    classes = models.ClassInfo.objects.filter(major_id=majorid)
    res = []
    for i in classes:
        res.append([i.id, i.class_id])
    return JsonResponse({'classes': res})


def showstudents(request):
    print(request.GET)
    college_id = request.GET.get('college_id')
    major_id = request.GET.get('major_id')
    class_id = request.GET.get('class_id')

    students = models.StudentInfo.objects.filter(Class=class_id)
    res = []
    for i in students:
        #res.append([i.stu_id, i.name]) #键值对传Json
        data = {
            'stu_id': i.stu_id,
            'name': i.name,
            'class': i.Class.class_id,
            'sex': i.sex
        }
        res.append(data)  # 列表存储字典，并转换成Json格式

    print(res)
    return JsonResponse(res, safe=False)


def edit_student(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_stuid = request.POST.get("stu_id")
        new_password = request.POST.get("passwd")
        new_name = request.POST.get("name")
        new_sex = request.POST.get("sex")
        new_id = request.POST.get("ID")
        new_birthday = request.POST.get("birthday")
        new_entrytime = request.POST.get("entrytime")
        new_grade = request.POST.get("grade")
        new_country = request.POST.get("country")
        new_city = request.POST.get("city")
        new_outlook = request.POST.get("outlook")
        new_class = request.POST.get("class")

        date = datetime.datetime.strptime(new_entrytime, "%Y-%m-%d")
        print(date)

        edit_student = models.StudentInfo.objects.get(id=edit_id)
        edit_student.stu_id = new_stuid
        edit_student.password = new_password
        edit_student.name = new_name
        edit_student.sex = new_sex
        edit_student.IDnumber = new_id
        edit_student.birthday = new_birthday
        edit_student.entrytime = new_entrytime
        edit_student.grade = new_grade
        edit_student.native_id = new_city
        edit_student.outlook_id = new_outlook
        edit_student.Class_id = new_class
        edit_student.save()
        return redirect("/admin/status/")

    edit_id = request.GET.get("id")
    edit_student_obj = models.StudentInfo.objects.get(stu_id=edit_id)
    stu_major = edit_student_obj.Class.major
    stu_college = edit_student_obj.Class.major.college
    stu_province = edit_student_obj.native.Province
    stu_country = edit_student_obj.native.Province.Country
    outlook = models.Outlook.objects.all()

    print(edit_student_obj.birthday)

    return render(request, "eas/admin/edit_student.html", {
        "stu": edit_student_obj,
        "outlook_list": outlook,
        "major": stu_major,
        "college": stu_college,
        "province": stu_province,
        "country": stu_country})


def judgename(request):
    temp = models.StudentInfo.objects.filter(stu_id=request.GET.get("stu_id"))
    if temp:
        return HttpResponse("学号重复，请检查")
    else:
        return HttpResponse('')


def delete_student(request):
    student = request.GET.get("id")
    models.StudentInfo.objects.get(stu_id=student).delete()
    return redirect("/admin/status/")


def add_student(request):
    if request.method == "POST":
        class_id = request.POST.get("id")
        print(class_id)
        new_stuid = request.POST.get("stu_id")
        new_password = request.POST.get("passwd")
        new_name = request.POST.get("name")
        new_sex = request.POST.get("sex")
        new_id = request.POST.get("ID")
        new_birthday = request.POST.get("birthday")
        new_entrytime = request.POST.get("entrytime")
        new_grade = request.POST.get("grade")
        new_country = request.POST.get("country")
        new_city = request.POST.get("city")
        new_outlook = request.POST.get("outlook")

        models.StudentInfo.objects.create(stu_id=new_stuid, password=new_password,
                                          name=new_name, birthday=new_birthday, IDnumber=new_id, sex=new_sex,
                                          entryTime=new_entrytime, grade=new_grade, outlook_id=new_outlook,
                                          nation=new_country, native_id=new_city, Class_id=class_id)
        return redirect("/admin/status/")

    class_id = request.GET.get("id")
    class_ = models.ClassInfo.objects.get(id=class_id)
    outlook = models.Outlook.objects.all()
    return render(request, 'eas/admin/add_student.html', {
        "class": class_,
        "outlook_list": outlook,
    })


def searchstatu(request):
    content = request.GET.get('content')

    students = models.StudentInfo.objects.filter(
        Q(stu_id=content) | Q(name=content))
    res = []
    for i in students:
        #res.append([i.stu_id, i.name]) #键值对传Json
        data = {
            'stu_id': i.stu_id,
            'name': i.name,
            'class': i.Class.class_id,
            'sex': i.sex
        }
        res.append(data)  # 列表存储字典，并转换成Json格式

    queryset = models.StudentInfo.objects.all()
    queryset.query.__str__()
    return JsonResponse(res, safe=False)


def searchroom(request):
    content = request.GET.get('content')
    if content != "":
        classrooms = models.ClassRoom.objects.filter(name=content)
    else:
        classrooms = models.ClassRoom.objects.all()
    res = []
    for i in classrooms:
        #res.append([i.stu_id, i.name]) #键值对传Json
        data = {
            'id':i.id,
            'name': i.name,
            'capacity': i.capacity,
            'function': i.function.name,
        }
        res.append(data)  # 列表存储字典，并转换成Json格式

    queryset = models.StudentInfo.objects.all()
    queryset.query.__str__()
    return JsonResponse(res, safe=False)


def classrooms(request):
    classrooms = models.ClassRoom.objects.all()

    return render(request, "eas/admin/admin_classrooms.html", {"classrooms": classrooms})


def delete_classroom(request):
    classroom = request.GET.get("id")
    models.StudentInfo.objects.get(id=classroom).delete()
    return redirect("/admin/classrooms/")


def edit_classroom(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_capacity = request.POST.get("capacity")
        new_function = request.POST.get("function")

        edit_classroom = models.ClassRoom.objects.get(id=edit_id)
        edit_classroom.capacity = new_capacity
        edit_classroom.function_id = new_function
        edit_classroom.save()
        return redirect("/admin/classrooms/")

    classroom_id = request.GET.get("id")
    edit_classroom_obj = models.ClassRoom.objects.get(id=classroom_id)
    room_capacity = edit_classroom_obj.capacity
    room_function = models.Function.objects.all()

    return render(request, "eas/admin/edit_classroom.html", {
        "room": edit_classroom_obj,
        "capacity": room_capacity,
        "function_list": room_function})


def getFunction(request):
    functions = models.Function.objects.all()
    res = []
    for i in functions:
        res.append([i.id, i.name])
    print(res)
    return JsonResponse({'functions': res})


def getBuilding(request):
    buildings = models.Building.objects.all()
    res = []
    for i in buildings:
        res.append([i.id, i.name])
    print(res)
    return JsonResponse({'buildings': res})


def getroomlist(request):
    function = request.GET.get('function_id')
    capacity = request.GET.get('capacity')
    building = request.GET.get('building')

    if capacity == "" and function == "0" and building == "0":
        classrooms = models.ClassRoom.objects.all()
    elif capacity == "" and function == "0":
        classrooms = models.ClassRoom.objects.filter(Q(building_id=building))
    elif capacity == "" and building == "0":
        classrooms = models.ClassRoom.objects.filter(Q(function_id=function))
    elif building == "0" and function == "0":
        classrooms = models.ClassRoom.objects.filter(Q(capacity__gt=int(capacity)-1))
    elif capacity == "":
        classrooms = models.ClassRoom.objects.filter(
            Q(building_id = building) & Q(function_id=function))
    elif function == "0":
        classrooms = models.ClassRoom.objects.filter(
            Q(building_id = building) & Q(capacity__gt=int(capacity)-1))
    elif building == "0":
        classrooms = models.ClassRoom.objects.filter(
            Q(function_id = function) & Q(capacity__gt=int(capacity)-1))
    else:
        classrooms = models.ClassRoom.objects.filter(
            Q(capacity__gt=int(capacity)-1) & Q(function_id=function) & Q(building_id = building))
    print(classrooms)
    res = []
    for i in classrooms:
        data = {
            'id': i.id,
            'name': i.name,
            'capacity': i.capacity,
            'functions': i.function.name,
        }
        res.append(data)  # 列表存储字典，并转换成Json格式

    return JsonResponse(res, safe=False)


def teacherlist(request):
    teacherlist = models.TeacherInfo.objects.all()
    return render(request, "eas/admin/admin_teacherinfo.html", {"teachers": teacherlist})


def getcourse(request):
    edit_id = request.GET.get("college_id")
    courses = models.Course.objects.filter(college=edit_id)
    res = []
    for i in courses:
        res.append([i.id, i.name])
    print(res)
    return JsonResponse({'courses': res})


def getteacher(request):
    college = request.GET.get('college_id')
    course = request.GET.get('course_id')
    print(college, course)
    if college == "0" and course == "0":
        teachers = models.TeacherInfo.objects.all()
    elif course == "0":
        teachers = models.TeacherInfo.objects.filter(college=college)
    else:
        teachers = models.TeacherInfo.objects.filter(
            Q(college=college) & Q(course=course))
    print(teachers)
    res = []
    for i in teachers:
        data = {
            'id': i.id,
            'tea_id': i.tea_id,
            'name': i.name,
            'sex': i.sex,
            'title': i.title.name,
        }
        res.append(data)  # 列表存储字典，并转换成Json格式

    return JsonResponse(res, safe=False)


def courselist(request):
    courses = models.Course.objects.filter(id__gt=0)
    return render(request, "eas/admin/admin_courses.html", {"courses": courses})


def getselcourse(request):
    college = request.GET.get('college_id')
    function = request.GET.get('function_id')
    elective = request.GET.get('elective')
    print(college, function, elective)
    if college == "0" and function == "0" and elective == "0":
        courses = models.Course.objects.filter(id__gt=0)
    elif college == "0" and function == "0":
        courses = models.Course.objects.filter(
            Q(elective=elective) & Q(id__gt=0))
    elif college == "0" and elective == "0":
        courses = models.Course.objects.filter(
            Q(function_id=function) & Q(id__gt=0))
    elif function == "0" and elective == "0":
        courses = models.Course.objects.filter(
            Q(college=college) & Q(id__gt=0))
    elif college == "0":
        courses = models.Course.objects.filter(
            Q(elective=elective) & Q(function_id=function) & Q(id__gt=0))
    elif function == "0":
        courses = models.Course.objects.filter(
            Q(college=college) & Q(elective=elective) & Q(id__gt=0))
    elif elective == "0":
        courses = models.Course.objects.filter(
            Q(college=college) & Q(function_id=function) & Q(id__gt=0))
    else:
        courses = models.Course.objects.filter(Q(college=college) & Q(
            function_id=function) & Q(elective=elective) & Q(id__gt=0))
    print(courses)
    res = []
    for i in courses:
        print(i.college.id, i.function.id)
        data = {
            'id': i.id,
            'cou_id': i.cou_id,
            'name': i.name,
            'classhour': i.classhour,
            'college': i.college.name,
            'function': i.function.name,
        }
        res.append(data)  # 列表存储字典，并转换成Json格式

    return JsonResponse(res, safe=False)


def edit_teacher(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_teaid = request.POST.get("tea_id")
        new_password = request.POST.get("passwd")
        new_name = request.POST.get("name")
        new_sex = request.POST.get("sex")
        new_id = request.POST.get("ID")
        new_birthday = request.POST.get("birthday")
        new_entrytime = request.POST.get("entrytime")
        new_country = request.POST.get("country")
        new_city = request.POST.get("city")
        new_outlook = request.POST.get("outlook")
        new_college = request.POST.get("college")
        new_title = request.POST.get("title")
        new_coursegroup = request.POST.getlist("coursegroup")

        print(new_coursegroup)

        edit_teacher = models.TeacherInfo.objects.get(id=edit_id)
        edit_teacher.tea_id = new_teaid
        edit_teacher.password = new_password
        edit_teacher.name = new_name
        edit_teacher.sex = new_sex
        edit_teacher.IDnumber = new_id
        edit_teacher.birthday = new_birthday
        edit_teacher.entrytime = new_entrytime
        edit_teacher.native_id = new_city
        edit_teacher.outlook_id = new_outlook
        edit_teacher.title_id = new_title
        edit_teacher.college_id = new_college
        edit_teacher.course.set(new_coursegroup)
        edit_teacher.save()
        return redirect("/admin/teacherlist/")

    tea_id = request.GET.get("id")
    edit_teacher_obj = models.TeacherInfo.objects.get(id=tea_id)
    outlooks = models.Outlook.objects.all()
    tea_college = edit_teacher_obj.college
    tea_province = edit_teacher_obj.native.Province
    tea_country = edit_teacher_obj.native.Province.Country
    title = models.Teacher_title.objects.all()
    tea_sel_course = edit_teacher_obj.course.all()
    courses = models.Course.objects.filter(college=edit_teacher_obj.college)
    print(tea_sel_course)
    print(courses)
    return render(request, "eas/admin/edit_teacher.html", {
        'teachers': 1,
        'tea': edit_teacher_obj,
        'outlook_list': outlooks,
        'college': tea_college,
        'country': tea_country,
        'province': tea_province,
        'titles': title,
        'course': courses,
        'teaselcourse': tea_sel_course,
    })


def getteacou(request):
    tea_id = request.GET.get("tea_id")
    course = models.TeacherInfo.objects.get(id=tea_id).course.all()
    res = []
    print(course)
    for cou in course:
        res.append(cou.id)
        print(cou.id)
    print("aaaaaaaaaa")
    return JsonResponse(res, safe=False)


def add_teacher(request):
    if request.method == "POST":
        new_teaid = request.POST.get("tea_id")
        new_password = request.POST.get("passwd")
        new_name = request.POST.get("name")
        new_sex = request.POST.get("sex")
        new_id = request.POST.get("ID")
        new_birthday = request.POST.get("birthday")
        new_entrytime = request.POST.get("entrytime")
        new_country = request.POST.get("country")
        new_city = request.POST.get("city")
        new_outlook = request.POST.get("outlook")
        new_college = request.POST.get("college")
        new_title = request.POST.get("title")
        new_coursegroup = request.POST.getlist("coursegroup")

        print(new_coursegroup)

        new_teacher_obj = models.TeacherInfo.objects.create(tea_id=new_teaid, password=new_password,
                                                            name=new_name, birthday=new_birthday, IDnumber=new_id, sex=new_sex,
                                                            entryTime=new_entrytime, college_id=new_college, outlook_id=new_outlook,
                                                            nation=new_country, native_id=new_city, title_id=new_title)
        new_teacher_obj.course.set(new_coursegroup)
        return redirect("/admin/teacherlist/")

    outlook = models.Outlook.objects.all()
    title = models.Teacher_title.objects.all()
    return render(request, "eas/admin/add_teacher.html", {
        'outlook_list': outlook,
        'titles': title,
    })


def delete_teacher(request):
    print("helloworld")
    tea_id = request.GET.get("id")
    models.TeacherInfo.objects.get(tea_id=tea_id).delete()
    return redirect("/admin/teacherlist/")
