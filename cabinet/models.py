from django.contrib.auth import password_validation
from django.db import models
from django.contrib.auth.models import AbstractUser, User
import datetime


class UserProfile(AbstractUser):
    status = models.CharField(max_length=128, blank=True)
    date_birthday = models.DateField(blank=True, null=True, default='1970-01-01', verbose_name='День рождения')
    telegram = models.CharField(max_length=64, default='Неизвестно', null=True, verbose_name='Telegram', blank=True)
    discord = models.CharField(max_length=64, default='Неизвестно', null=True, verbose_name='Discord', blank=True)
    gender = models.CharField(max_length=16, default='Не указан', null=True, verbose_name='Пол')
    reputation = models.IntegerField(verbose_name='Репутация', default=0)
    messages = models.IntegerField(verbose_name='Сообщения', default=0)
    subscribes = models.IntegerField(verbose_name='Подписчики', default=0)
    product = models.IntegerField(verbose_name='Товаров', default=0)
    avatar = models.ImageField(upload_to='images_profile/%Y-%m-%d', default='images_profile/2023-05-27/caf098e477ae55905890b7fb0b3700c1.jpg')

    def save(self, *args, **kwargs):
        self.last_login = datetime.datetime.now()
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
