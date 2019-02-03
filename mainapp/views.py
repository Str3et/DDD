from django.shortcuts import render
from django.http import HttpRequest
from .models import ProductCategory, Product

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
        'products': Product.objects.get(id=1),
        'prod_menu_1': ProductCategory.objects.get(id=1),
        'prod_menu_2': ProductCategory.objects.get(id=2),
        'prod_menu_3': ProductCategory.objects.get(id=3),
        'prod_menu_4': ProductCategory.objects.get(id=4),
        'prod_menu_5': ProductCategory.objects.get(id=5),
    }
    return render(request, 'mainapp/interior.html', context=context)


def products(request: HttpRequest, pk=None):
    print(pk)
    context = {
        'page_title': 'Каталог товаров',
    }
    return render(request, 'mainapp/products.html', context=context)


def test(request: HttpRequest):
    context = {
        'page_title': 'Тест',
    }
    return render(request, 'mainapp/child.html', context=context)
