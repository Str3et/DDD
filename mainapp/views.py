from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import ProductCategory, Product
from basketapp.models import Basket

# Create your views here.


def index(request: HttpRequest):
    products = Product.objects.all()
    context = {
        'page_title': 'Home',
        'products': products,
        'basket': get_current_basket(request.user),
        }
    return render(request, 'mainapp/index.html', context=context)


def contact(request: HttpRequest):
    context = {
        'page_title': 'Контакты',
        'basket': get_current_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', context=context)


def interior(request: HttpRequest):
    context = {
        'page_title': 'Лучшее предложение',
        'products': Product.objects.get(id=1),
    }
    return render(request, 'mainapp/interior.html', context=context)


def product_detail(request: HttpRequest, id=None):
    if id is not None:
        item = get_object_or_404(Product, id=id)
        same_products = Product.objects.exclude(pk=id).filter(category__pk=item.category_id)
        links_menu = ProductCategory.objects.all()
        context = {
            'page_title': f'Товар: {item.name}',
            'item': item,
            'products': same_products,
            'links_menu': links_menu,
            'basket': get_current_basket(request.user),
        }
        return render(request, 'mainapp/details.html', context)


def products(request: HttpRequest, id=None):
    links_menu = ProductCategory.objects.all()

    if id is not None:
        same_products = Product.objects.filter(category__pk=id)
    else:
        same_products = Product.objects.all()
    context = {
        'page_title': 'Каталог товаров',
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': get_current_basket(request.user),
    }
    return render(request, 'mainapp/products.html', context=context)

#  проверка на анонимность корзины.
def get_current_basket(current_user):
    if current_user.is_authenticated:
        basket = Basket.objects.filter(user=current_user)
    else:
        basket = None
    return basket
