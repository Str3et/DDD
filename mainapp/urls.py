from django.urls import path
import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('', controller.products, name='index'),
    path('category/<int:id>/', controller.products, name='category'),
    path('details/<int:id>/', controller.product_detail, name='details'),
]
