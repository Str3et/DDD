from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from authapp.models import CustomUser


class UserListView(ListView):
    model = CustomUser
    template_name = 'adminapp/users/index.html'

    def get_context_data(self, **kwargs):
        parent_context = super(UserListView, self).get_context_data(**kwargs)
        parent_context['page_title'] = 'Admin -> Main users'
        return parent_context

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'adminapp/users/create.html'
    fields = '__all__'
    success_url = reverse_lazy('admin:users')

    def get_context_data(self, **kwargs):
        parent_context = super(UserCreateView, self).get_context_data(**kwargs)
        parent_context['page_title'] = 'Admin -> Create user'
        return parent_context


class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'adminapp/users/update.html'
    fields = 'username', 'age', 'email', 'first_name', 'avatar', 'is_active'
    success_url = reverse_lazy('admin:users')

    def get_context_data(self, **kwargs):
        parent_context = super(UserUpdateView, self).get_context_data(**kwargs)
        parent_context['page_title'] = 'Admin -> Update user'
        return parent_context


class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'adminapp/users/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('admin:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        parent_context = super(UserDeleteView, self).get_context_data(**kwargs)
        parent_context['page_title'] = 'Admin -> Delete user'
        return parent_context


class UserReadView(DetailView):
    model = CustomUser
    template_name = 'adminapp/users/read.html'
    fields = '__all__'
    # success_url = reverse_lazy('admin:users')
