from django.db import models
from django.db.models.base import Model
from django.utils import timezone
import datetime

# Create your models here.


class StudentInfo (models.Model):
    id = models.AutoField(primary_key=True)
    stu_id = models.CharField(
        null=False, max_length=20, default="", unique=True)
    password = models.CharField(null=False, max_length=50, default="123456")
    name = models.CharField(null=False, max_length=20, default="")
    birthday = models.DateField(default=timezone.now)
    IDnumber = models.CharField(null=False, max_length=20, default="")
    sex = models.CharField(null=False, max_length=5, default="")
    entryTime = models.DateField(default=timezone.now)
    grade = models.IntegerField()
    outlook = models.ForeignKey(to="Outlook", on_delete=models.CASCADE)
    nation = models.IntegerField(default=0)
    #native = models.IntegerField(default=0)
    native = models.ForeignKey(to="Cities", on_delete=models.CASCADE)
    Class = models.ForeignKey(to="ClassInfo", on_delete=models.CASCADE)
    credit = models.FloatField(default=0)
    #选课
    elecourse = models.ManyToManyField(to="Course", through="Student2Course",
                                       through_fields=("student_id", "course_id"))


class ClassInfo (models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.CharField(
        null=False, max_length=20, default="", unique=True)
    major = models.ForeignKey(to="MajorInfo", on_delete=models.CASCADE)


class MajorInfo (models.Model):
    id = models.AutoField(primary_key=True)
    major_id = models.IntegerField()
    name = models.CharField(null=False, max_length=20, default="")
    college = models.ForeignKey(to="CollegeInfo", on_delete=models.CASCADE)
    #专业和课程没有现时关系，直接使用多对多关联
    course = models.ManyToManyField(to="Course")


class CollegeInfo (models.Model):
    id = models.AutoField(primary_key=True)
    college_id = models.IntegerField(unique=True)
    name = models.CharField(null=False, max_length=20, default="")


class CollegeInfo4tc (models.Model):
    id = models.AutoField(primary_key=True)
    college_id = models.IntegerField(unique=True)
    name = models.CharField(null=False, max_length=20, default="")


class AdminInfo (models.Model):
    id = models.AutoField(primary_key=True)
    adm_id = models.CharField(
        null=False, max_length=20, default="", unique=True)
    password = models.CharField(null=False, max_length=50, default="123456")


class TeacherInfo(models.Model):
    id = models.AutoField(primary_key=True)
    tea_id = models.CharField(
        null=False, max_length=20, default="", unique=True)
    password = models.CharField(null=False, max_length=50, default="123456")
    name = models.CharField(null=False, max_length=20, default="")
    birthday = models.DateField(default=timezone.now)
    IDnumber = models.CharField(null=False, max_length=20, default="")
    sex = models.CharField(null=False, max_length=5, default="")
    entryTime = models.DateField(auto_now_add=True)
    title = models.ForeignKey(to="Teacher_title", on_delete=models.CASCADE)
    outlook = models.ForeignKey(to="Outlook", on_delete=models.CASCADE)
    nation = models.IntegerField(default=0)
    native = models.ForeignKey(to="Cities", on_delete=models.CASCADE)
    #courseGroup = models.ForeignKey (to = "Course_Group" , on_delete = models.CASCADE)
    #教师和课程（课程组）也没有现时关系，直接使用多对多关联
    course = models.ManyToManyField(to="Course")
    college = models.ForeignKey(
        to="CollegeInfo4tc", on_delete=models.CASCADE, default=2)


#
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    cou_id = models.CharField(
        null=False, max_length=10, default="", unique=True)
    name = models.CharField(null=False, max_length=10, default="", unique=True)
    #学时
    classhour = models.IntegerField()
    hourperweek = models.FloatField(default=1.0)
    #学分
    credit = models.FloatField()
    #建议修读年份
    betyear = models.IntegerField()
    #是否选修
    elective = models.BooleanField(default=False)
    #课程类型 普通 ordinary 上机 opc  实验exper
    function = models.ForeignKey(
        to="Function", on_delete=models.CASCADE, default=1)
    priority = models.IntegerField(default=1)
    #所属学院
    college = models.ForeignKey(to="CollegeInfo4tc", on_delete=models.CASCADE)
    #先导课
    pre_course = models.ForeignKey(to="self",on_delete=models.CASCADE, default=1 , null = True)


class Results(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(to="StudentInfo", on_delete=models.CASCADE)
    teacher = models.ForeignKey(to="TeacherInfo", on_delete=models.CASCADE)
    course = models.ForeignKey(to="Course", on_delete=models.CASCADE)
    result = models.IntegerField()
    examtime = models.DateField(auto_now_add=True)


class Teacher2Time(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(to="TeacherInfo", on_delete=models.CASCADE)
    time_id = models.ForeignKey(to="ClassTime", on_delete=models.CASCADE)
    course_id = models.ForeignKey(to="Course", on_delete=models.CASCADE)
    classroom = models.ForeignKey(to="Classroom", on_delete=models.CASCADE)


class Student2Course(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(to="StudentInfo", on_delete=models.CASCADE)
    course_id = models.ForeignKey(to="Course", on_delete=models.CASCADE)
    isfinished = models.BooleanField(default=False)


#课程/教室功能
class ClassRoom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=10, default="", unique=True)
    capacity = models.IntegerField()
    function = models.ForeignKey(
        to="Function", on_delete=models.CASCADE, default=1)
    building = models.ForeignKey(to="Building",on_delete=models.CASCADE, default=1)

#课程类型 普通 ordinary 上机 opc  实验exper


class Function(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=10,
                            default="ordinary", unique=True)

 # 建立城市自关联数据库表


class Areas(models.Model):
    aid = models.IntegerField(default=0)
    atitle = models.CharField(max_length=30)
    aParent = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.atitle


class Countries(models.Model):
    aid = models.IntegerField(default=0)
    atitle = models.CharField(max_length=30)

    def __str__(self):
        return self.atitle


class Provinces(models.Model):
    aid = models.IntegerField(default=0)
    atitle = models.CharField(max_length=30)
    Country = models.ForeignKey(to="Countries", on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle


class Cities(models.Model):
    aid = models.IntegerField(default=0)
    atitle = models.CharField(max_length=30)
    Province = models.ForeignKey(to="Provinces", on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle


class Outlook(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class Teacher_title(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class ClassTime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    direct = models.CharField(max_length=5)


#身份证也需要一张单独的表


#选修课也需要一张单独的表


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(to="StudentInfo", on_delete=models.CASCADE , null=True)
    teacher = models.ForeignKey(to="TeacherInfo", on_delete=models.CASCADE , null=True)
    admin = models.ForeignKey(to="AdminInfo", on_delete=models.CASCADE , null=True)
    fromwho = models.CharField(max_length=30, default="none")
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000 , null=True)
    gettime = models.DateTimeField(default=timezone.now)
    finishtime = models.DateTimeField(default=timezone.now)
    isFinished = models.IntegerField(default=0)
    result= models.CharField(max_length=30, default="none")

    class Meta:
        ordering = ['-isFinished', ['-gettime'],['-finishtie']]