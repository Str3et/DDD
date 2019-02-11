from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from mainapp.models import Product
from adminapp.models.products import ProductsEditForm, ProductCreateForm


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCreateForm()

    return render(request, 'adminapp/products/create.html', {
        'form': form,
    })


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'adminapp/products/read.html', {
        'product': product,
    })
    return HttpResponse('action -> read')


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id):
    model = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductsEditForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
    else:
        form = ProductsEditForm(instance=model)

    return render(request, 'adminapp/products/update.html', {
        'form': form,
    })


@user_passes_test(lambda user: user.is_superuser)
def list_by_category(request: HttpRequest, category):
    return HttpResponse('action -> list')


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    model = get_object_or_404(Product, id=id)
    # model.delete()

    return HttpResponseRedirect(reverse('admin:categories'))
