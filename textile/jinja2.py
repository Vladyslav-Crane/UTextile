from jinja2 import Environment, FileSystemLoader, select_autoescape
from django.apps import apps


def environment(**options):
    template_dirs = [f"{app.path}/jinja_templates" for app in apps.get_app_configs()]

    options.update(
        {
            "loader": FileSystemLoader(template_dirs),
            "autoescape": select_autoescape(["html", "xml"]),
        }
    )
    env = Environment(**options)
    env.globals.update(
        {
            "static": "django.templatetags.static.static",
            "url": "django.urls.reverse",
        }
    )
    return env
