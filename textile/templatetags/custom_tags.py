from datetime import datetime
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def current_time(format_str):
    return datetime.now().strftime(format_str)

@register.simple_tag
def build_title(title):
    return f'{title} | {settings.SITE_NAME}'
