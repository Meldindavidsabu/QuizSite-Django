
from django import template

register = template.Library()

@register.filter(name='capitalize_text')
def capitalize_text(value):
    return value.capitalize() if isinstance(value, str) else value
