from django import template
from adminstrator import views

register = template.Library()

@register.inclusion_tag('eas/admin/student_list.html')
def show_student_list():
    print (views.showstudents.class_id)
    return {'student_list': a}
