from django.shortcuts import render, redirect
from django.views.generic import RedirectView
from .forms import ContactForm


def index(request):
    return render(request, "index.html")

def http_404_handler(request, exc):
    return render(request, "http_404.html")


def contacts_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # Например, отправка email или сохранение в базе данных
            return redirect("home")
    else:
        form = ContactForm()
    return render(request, "contacts.html", {"form": form})
