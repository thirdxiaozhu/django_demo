from django import template

#注册
register = template.Library()

@register.filter(name = "sb")
def add_sb(arg):
    return "{} sb.".format(arg)


@register.filter(name = "add_two")
def add_sb(arg, arg_2):
    return "{} {}".format(arg, arg_2)
