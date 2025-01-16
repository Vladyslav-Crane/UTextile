import os
from django.utils.translation import gettext_lazy as _

from .common import *

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = ["127.0.0.1"]
DEBUG = True


SITE_NAME = _("UTextile")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "builtins": ["textile.templatetags.custom_tags"],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "textile.context_processors.meta",
            ],
        },
    },
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [BASE_DIR / "jinja_templates"],  # Папка для Jinja2 шаблонов
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "textile.jinja2.environment",
        },
    },
]

# PROJECT_ROOT = path(__file__).abspath().dirname().dirname()  # /edx-platform/lms
# REPO_ROOT = PROJECT_ROOT.dirname()
LOCALE_PATHS = [BASE_DIR / "conf/locale", PROJECT_DIR / "catalog/conf/locale"]

LANGUAGE_CODE = "en"
