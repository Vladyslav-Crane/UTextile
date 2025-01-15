from django.shortcuts import render
from django.views.generic import RedirectView


class HomepageRedirect(RedirectView):
    pattern_name = "catalog:catalog"


def http_404_handler(request, exc):
    return render(request, "http_404.html")
