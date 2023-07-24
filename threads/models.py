from django.db import models
from cabinet.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Категория', unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Thread(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Создатель')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.CharField(max_length=10000, verbose_name='Текст')
    screen = models.ImageField(verbose_name='Медиа', upload_to='images_threads/%Y-%m-%d', null=True, default=None)
    likes = models.IntegerField(verbose_name='Лайков', default=0)
    comments = models.IntegerField(verbose_name='Ответов', default=0)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title