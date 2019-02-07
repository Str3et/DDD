from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .forms import LoginForm, RegisterForm, UpdateForm
from mainapp.views import get_current_basket


def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect('/auth/login')


def login(request: HttpRequest):
    title = 'Вход на сайт'
    # создаём форму для заполнения
    login_form = LoginForm(data=request.POST or None)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    #  проверяем дланные из request
    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']
        # next_url = request.POST['next'] or '/'
        # выполнить аутентификацию
        user = auth.authenticate(username=login, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect('/')
    content = {
        'page_title': title,
        'login_form': login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', content)


def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request: HttpRequest):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = RegisterForm()

    content = {
        'page_title': title,
        'reg_form': register_form
    }

    return render(request, 'authapp/register.html', content)


def edit(request: HttpRequest):
    title = 'Профиль'

    if request.method == 'POST':
        update_form = UpdateForm(request.POST, request.FILES, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        update_form = UpdateForm(instance=request.user)

    content = {
        'page_title': title,
        'update_form': update_form,
        'basket': get_current_basket(request.user),
    }

    return render(request, 'authapp/edit.html', content)
