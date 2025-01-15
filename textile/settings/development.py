import os
from django.utils.translation import gettext_lazy as _

from .common import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = ['127.0.0.1']
DEBUG = True


SITE_NAME = _('UTextile')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
