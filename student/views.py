from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.shortcuts import render , HttpResponse , redirect
from django.urls import path
from django.contrib.auth import authenticate
from student import models
from adminstrator import models as adm_mod
from django.http import HttpResponseRedirect
from django.db.models import Q
import datetime

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
    messages = adm_mod.Message.objects.filter(student_id = student.id).order_by('-isFinished','-gettime')
    return render(request, "eas/student/student_sendbox.html",{'messages':messages})


def filmessage(request):
    startdate = request.POST.get("startdate")
    enddate = request.POST.get("enddate")
    student = adm_mod.StudentInfo.objects.get(stu_id=request.session.get('userid'))
    #传入的enddate是指向该日期的00：00：00,如果要按照常规逻辑需要把该字符串日期转换成日期格式并+1
    #通过保存一个备份，最后再返回一个备份过的enddate值，这样就能在前端正常显示了
    enddate_backup = enddate
    if startdate == "" and enddate == "":
        remessages = adm_mod.Message.objects.filter(
            Q(student_id=student.id) & Q(fromwho="student")).order_by('-isFinished','-gettime')
    elif startdate == "":
        enddate = datetime.datetime.strptime(enddate,'%Y-%m-%d') + datetime.timedelta(days=1)
        remessages = adm_mod.Message.objects.filter(Q(student_id=student.id) & Q(fromwho="student") & Q(gettime__lte=enddate)).order_by('-isFinished','-gettime')
        enddate = enddate_backup
    elif enddate == "":
        remessages = adm_mod.Message.objects.filter(Q(student_id=student.id) & Q(fromwho="student") & Q(gettime__gte=startdate)).order_by('-isFinished','-gettime')
        print(remessages)
    else:
        enddate = datetime.datetime.strptime(enddate,'%Y-%m-%d') + datetime.timedelta(days=1)
        remessages = adm_mod.Message.objects.filter(Q(student_id = student.id) & Q(fromwho="student") & Q(gettime__gte=startdate) & Q(gettime__lte=enddate)).order_by('-isFinished','-gettime')
        enddate = enddate_backup

    return render(request, "eas/student/student_sendbox.html", {
        'messages': remessages,
        'startdate':startdate,
        'enddate':enddate,
        })