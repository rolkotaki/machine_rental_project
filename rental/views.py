from django.shortcuts import render
from .models import Contact, Machine, Price

def home(request):
    return render(request, 'home.html')


def machines(request):
    machine_list = list(Machine.objects.filter())
    return render(request, 'machines.html', {'machine_list': machine_list})


def contact(request):
    contact = Contact.objects.get(id=1)
    return render(request, 'contact.html', {'contact': contact})


def machine(request, machine_id):
    machine_ = Machine.objects.get(machine_id=machine_id)
    prices = Price.objects.filter(machine_id=machine_id)
    return render(request, 'machine.html', {'machine_': machine_, 'prices': prices})

def order(request):
    return render(request, '')
