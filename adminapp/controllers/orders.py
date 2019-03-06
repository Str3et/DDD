from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from ordersapp.models import Order


class OrderListView(ListView):
    model = Order
    template_name = 'adminapp/orders/index.html'

    def get_context_data(self, **kwargs):
        parent_context = super(OrderListView, self).get_context_data(**kwargs)
        parent_context['page_title'] = 'Admin -> Main orders'
        return parent_context

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(OrderListView, self).dispatch(request, *args, **kwargs)


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'adminapp/orders/update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin:orders')

    def get_context_data(self, **kwargs):
        parent_context = super(OrderUpdateView, self).get_context_data(**kwargs)
        parent_context['page_title'] = 'Admin -> Update order'
        return parent_context
