from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.shortcuts import render , HttpResponse , redirect
from django.urls import path
from django.contrib.auth import authenticate
from student import models
from adminstrator import models as adm_mod
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    stuid = request.session.get('userid')
    stu_name = adm_mod.StudentInfo.objects.get(stu_id = stuid).name
    return render(request, "eas/student/student_index.html", {'student': stu_name})


def showstatu(request):
    print(request.session['usertype'])
    edit_student_obj = adm_mod.StudentInfo.objects.get(stu_id=request.session.get('userid'))
    stu_major = edit_student_obj.Class.major
    stu_college = edit_student_obj.Class.major.college
    stu_province = edit_student_obj.native.Province
    stu_country = edit_student_obj.native.Province.Country
    outlook = adm_mod.Outlook.objects.all()

    print(edit_student_obj.birthday)

    return render(request, "eas/student/showstatu.html", {
        "stu": edit_student_obj,
        "outlook_list": outlook,
        "major": stu_major,
        "college": stu_college,
        "province": stu_province,
        "country": stu_country})
    

def changepwd(request):
    student = adm_mod.StudentInfo.objects.get(stu_id=request.session.get('userid'))
    new_message = adm_mod.Message.objects.create(student_id = student.id,title="修改密码申请", admin_id=1 , fromwho="student")

    return HttpResponse("申请已成功提交")

    
def sendbox(request):
    student = adm_mod.StudentInfo.objects.get(stu_id=request.session.get('userid'))
    messages = adm_mod.Message.objects.filter(student_id = student.id).order_by('-isFinished')
    return render(request, "eas/student/student_sendbox.html",{'messages':messages})