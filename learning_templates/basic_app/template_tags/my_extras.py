from django import template

register = template.Library()

def cut(value,arg):

    """
    cuts out all values of "arg" form the string
    """
    return value.replace(arg,'')

register.filter('cut',cut)
