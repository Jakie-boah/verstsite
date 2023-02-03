

from django.shortcuts import render, redirect


def index(request):
    return render(request, './index.html')


def register(request):
    return render(request, './register.html')


def log_in(request):
    return render(request, './login.html')


def check(request):
    return render(request, './check_order.html')


def reviews(request):
    return render(request, './reviews.html')


def vacancy(request):
    return render(request, './vacancy.html')


def contacts(request):
    return render(request, './contacts.html')


def sales(request):
    return render(request, './sales.html')


def buy(request):
    return render(request, './buy.html')


def choose(request):
    return render(request, './choose.html')


def choose1(request):
    return render(request, './choose1.html')


def end(request):
    return render(request, './end.html')


def add(request):
    return render(request, './add.html')
