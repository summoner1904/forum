from django.db import models
from cabinet.models import UserProfile


class Thread(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Создатель')
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.CharField(max_length=10000, verbose_name='Текст')
    screen = models.ImageField(verbose_name='Медиа', upload_to='images_threads/%Y-%m-%d', null=True, default=None)
    likes = models.IntegerField(verbose_name='Лайков', default=0)
    comments = models.IntegerField(verbose_name='Ответов', default=0)