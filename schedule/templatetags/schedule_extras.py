from django import template
register = template.Library()


@register.filter(name='get_elem')
def get_elem(dictionary, key):
    return dictionary[key]