from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import HttpRequest
from django.urls import reverse
from django.db import  transaction
from .forms import LoginForm, RegisterForm, UpdateForm
from django.core.mail import send_mail
from django.conf import settings
from authapp.forms import CustomUserProfileUpdateForm
from authapp.models import CustomUser


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
            user = register_form.save()
            if send_verify_mail(user):
                print('Сообщение для подтверждения регистрации отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('Ошибка отправки сообщения для подтверждения регистрации')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = RegisterForm()

    content = {
        'page_title': title,
        'reg_form': register_form
    }

    return render(request, 'authapp/register.html', content)


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} \
        перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    print(f'from: {settings.EMAIL_HOST_USER}, to: {user.email}')
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = CustomUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            print(f'user {user} is activated')
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return render(request, 'authapp/Verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/Verification.html')

    except Exception as e:
        print(f'error activation user : {e.args}')

    return HttpResponseRedirect(reverse('main'))


@transaction.atomic
def edit(request: HttpRequest):
    title = 'Профиль'

    if request.method == 'POST':
        update_form = UpdateForm(request.POST, request.FILES, instance=request.user)
        profile_form = CustomUserProfileUpdateForm(request.POST, instance=request.user.customuserprofile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        update_form = UpdateForm(instance=request.user)
        profile_form = CustomUserProfileUpdateForm(instance=request.user.customuserprofile)

    content = {
        'page_title': title,
        'update_form': update_form,
        'profile_form': profile_form,
    }

    return render(request, 'authapp/edit.html', content)
