from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0)
    avatar = models.ImageField(upload_to='avatar_img', verbose_name='avatar', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
