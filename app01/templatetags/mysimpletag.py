from django import template

register = template.Library()

@register.simple_tag(name="mysum") #注册
def my_sum(arg1 , arg2 , arg3): #模板方法
    return "{} {} {}".format(arg1, arg2, arg3)

@register.inclusion_tag('1_1/results.html')
def show_results(n):
    n = 1 if n < 1 else int(n) #三目运算：为真时的结果 if 判断条件 else 为假时的结果（注意，没有冒号）
    data = ["第{}项".format(i) for i in range(1 , n+1)]
    return {'results': data}
