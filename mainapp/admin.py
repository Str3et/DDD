from django.contrib import admin
from .models import Product, ProductCategory, Person

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Person)
