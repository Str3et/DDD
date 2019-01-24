from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def index(request: HttpRequest):
    context = {
        'page_title': 'Home',
        }
    return render(request, 'mainapp/index.html', context=context)


def contact(request: HttpRequest):
    context = {
        'page_title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context=context)


def interior(request: HttpRequest):
    context = {
        'page_title': 'Лучшее предложение',
    }
    return render(request, 'mainapp/interior.html', context=context)


def products(request: HttpRequest):
    context = {
        'page_title': 'Каталог товаров',
    }
    return render(request, 'mainapp/products.html', context=context)


def test(request: HttpRequest):
    context = {
        'page_title': 'Тест',
    }
    return render(request, 'mainapp/child.html', context=context)
