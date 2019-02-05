from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
from mainapp.models import ProductCategory, Product
from authapp.models import CustomUser
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        ProductCategory.objects.all().delete()

        with open('static/Category.json', 'r', encoding="UTF-8") as f:
            data = json.load(f)
        for el in data:
            new_cat = ProductCategory(**el)
            new_cat.save()

        Product.objects.all().delete()
        with open('static/Products.json', 'r', encoding="UTF-8") as f:
            data = json.load(f)
        for el in data:
            new_prod = Product(**el)
            new_prod.save()


        # User.objects.create_superuser('ADmin', 'tt@test.ru', '123123')  --> создание для базовой модели.

        CustomUser.objects.create_superuser('ADmin', 'tt@test.ru', '123123', age=20)
        CustomUser.objects.create_user('min', 'ss@test.ru', '123123', age=20)
