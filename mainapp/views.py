from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'mainapp/index.html')

def contact(request: HttpRequest):
    return render(request, 'mainapp/contact.html')

def interior(request: HttpRequest):
    return render(request, 'mainapp/interior.html')

def products(request: HttpRequest):
    return render(request, 'mainapp/products.html')
