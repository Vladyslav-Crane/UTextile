from datetime import timedelta
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

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#         },
#         'textile.middleware': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# MIDDLEWARE.append('textile.middleware.CustomMiddleware')1

INSTALLED_APPS += [
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": SECRET_KEY,  # или можно другой секрет
    # Включаем ротацию: после refresh старый токен перестает работать
    "ROTATE_REFRESH_TOKENS": True,
    # Сразу помещать старый refresh-токен в blacklisted
    "BLACKLIST_AFTER_ROTATION": True,
}

TIME_ZONE = "Asia/Istanbul"
