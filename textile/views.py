from django.shortcuts import render


def http_404_handler(request, exc):
    return render(request, 'http_404.html')