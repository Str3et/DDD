from django.db import models

# Create your models here.

# class Person(models.Model):
#     name = models.CharField(max_length=25, verbose_name='Имя')
#     last_name = models.CharField(max_length=25, verbose_name='Фамилия')
#     age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=0)
#
#     def __str__(self):
#         return f'{self.name} {self.last_name}'


class ProductCategory(models.Model):
    name = models.CharField(max_length=55, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название продукта')
    image = models.ImageField(upload_to='prod_img', verbose_name='Картинка товара', blank=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    storage = models.IntegerField(verbose_name='Склад', default=0)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
