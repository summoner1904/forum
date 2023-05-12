from django.db import models
from django.contrib.auth.models import AbstractUser, User

class UserProfile(AbstractUser):
    status = models.CharField(max_length=128)
    date_birthday = models.DateField(blank=True, null=True, default=None)
    telegram = models.CharField(max_length=64, default=None, null=True)
    discord = models.CharField(max_length=64, default=None, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
