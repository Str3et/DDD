from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from adminapp.models.users import UsersEditForm
from authapp.forms import CustomUser, RegisterForm


@user_passes_test(lambda user: user.is_superuser)
def index(request: HttpRequest):
    models = CustomUser.objects.all()
    content = {
        'page_title': 'Admin -> user',
        'models': models,
    }
    return render(request, 'adminapp/users/index.html', content)


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        form = RegisterForm()

    return render(request, 'adminapp/users/create.html', {
        'form': form,
    })


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id):
    model = get_object_or_404(CustomUser, id=id)

    if request.method == 'POST':
        form = UsersEditForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
    else:
        form = UsersEditForm(instance=model)

    return render(request, 'adminapp/users/update.html', {
        'form': form,
    })


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'adminapp/users/read.html', {
        'user': user,
    })


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    user = get_object_or_404(CustomUser, id=id)
    # model.delete()
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))
    return render(request, 'adminapp/users/delete.html', {
        'user': user,
    })
