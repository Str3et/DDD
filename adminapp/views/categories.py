from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from mainapp.models import ProductCategory
from adminapp.models.categories import CategoryEditForm, CategoryCreateForm


@user_passes_test(lambda user: user.is_superuser)
def index(request: HttpRequest):
    models = ProductCategory.objects.all()
    return render(request, 'adminapp/categories/index.html', {
        'models': models,
    })


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = CategoryCreateForm()

    return render(request, 'adminapp/categories/create.html', {
        'form': form,
    })


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, id):
    # model = ProductCategory.objects.get(id=id)
    model = get_object_or_404(ProductCategory, id=id)
    products = model.products.all()
    return render(request, 'adminapp/categories/read.html', {
        'model': model,
        'products': products,
    })


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id):
    model = get_object_or_404(ProductCategory, id=id)

    if request.method == 'POST':
        form = CategoryEditForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
    else:
        form = CategoryEditForm(instance=model)

    return render(request, 'adminapp/categories/update.html', {
        'form': form,
    })


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    model = get_object_or_404(ProductCategory, id=id)
    # model.delete()

    return HttpResponseRedirect(reverse('admin:categories'))
