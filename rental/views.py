from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def machines(request):
    return render(request, 'machines.html')


def contact(request):
    return render(request, 'contact.html')


def order(request):
    return render(request, '')
