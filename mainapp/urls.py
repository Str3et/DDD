from django.urls import path
import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('', controller.products, name='index'),
    path('<int:pk>/', controller.products, name='category'),
]
