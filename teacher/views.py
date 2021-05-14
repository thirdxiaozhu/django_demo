from django.shortcuts import render
from adminstrator import models as adm_mod

# Create your views here.

def index(request):
    tea_id = request.session.get('userid')
    tea_name = adm_mod.TeacherInfo.objects.get(tea_id = tea_id).name
    return render(request, "eas/teacher/teacher_index.html", {'teacher': tea_name})