from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from mainapp.models import Product
from basketapp.models import Basket

@login_required
def add(request: HttpRequest, id: int):
    product = get_object_or_404(Product, pk=id)
    exists_item = Basket.objects.filter(user=request.user, product__id=id)
    if exists_item:
        exists_item[0].quantity += 1
        exists_item[0].save()
    else:
        new_item = Basket(user=request.user, product=product)
        new_item.quantity = 1
        new_item.save()

    if request.is_ajax():
        items = Basket.objects.filter(user=request.user)
        total_items = sum([x.quantity for x in items])

        cost = Basket.objects.filter(user=request.user)
        total_cost = sum([x.product_cost for x in cost])

        return JsonResponse({
            'quantity': Basket.objects.get(product_id=id).quantity,
            'price': Basket.objects.get(product_id=id).product.price,
            'total_quantity': total_items,
            'total_cost': total_cost,
        })

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect('/products/details/' + str(product.id))
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove(request: HttpRequest, id: int):
    item = get_object_or_404(Basket, id=id)
    item.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def index(request: HttpRequest):
    context = {
        'page_title': 'Корзина',
        }
    return render(request, 'basketapp/index.html', context=context)

@login_required
def delete(request: HttpRequest, id: int):
    product = get_object_or_404(Product, pk=id)
    exists_item = Basket.objects.filter(user=request.user, product__id=id)
    if exists_item:
        exists_item[0].quantity -= 1
        exists_item[0].save()

    if request.is_ajax():
        items = Basket.objects.filter(user=request.user)
        total_items = sum([x.quantity for x in items])

        cost = Basket.objects.filter(user=request.user)
        total_cost = sum([x.product_cost for x in cost])

        return JsonResponse({
            'quantity': Basket.objects.get(product_id=id).quantity,
            'total_quantity': total_items,
            'total_cost': total_cost,
            'price': Basket.objects.get(product_id=id).product.price,
        })

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect('/products/details/' + str(product.id))
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
