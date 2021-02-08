from django import template

register = template.Library()

@register.filter
def py_format(value, format_str):
    return "{0:{1}}".format(value, format_str)
