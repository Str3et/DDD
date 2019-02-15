from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from mainapp.models import ProductCategory


class UserCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories/index.html'

    def get_context_data(self, **kwargs):
        parent_context = super(UserCategoryListView, self).get_context_data(**kwargs)
        parent_context['page_title'] = 'Admin -> Main users'
        return parent_context

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCategoryListView, self).dispatch(request, *args, **kwargs)
