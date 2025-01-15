from django.conf import settings

def meta(request):
    return {
        'site_name': settings.SITE_NAME,
    }