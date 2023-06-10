from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    link = models.CharField(max_length=256, verbose_name='Ссылка')
    phone = models.CharField(max_length=8, verbose_name='Привязка к телефону')
    mail = models.CharField(max_length=64, verbose_name='Привязка к почте')
    nickname = models.CharField(max_length=128, verbose_name='Никнейм')
    lvl = models.IntegerField(verbose_name='Уровень', default=0, null=True)
    country = models.CharField(max_length=64, verbose_name='Страна')
    last_activity = models.DateField(verbose_name='Последняя активность')
    skins = models.IntegerField(verbose_name='Скины')

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
