from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0)
    avatar = models.ImageField(upload_to='avatar_img', verbose_name='avatar')
