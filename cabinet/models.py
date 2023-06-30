from django.contrib.auth import password_validation, get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser, User
import datetime


class UserProfile(AbstractUser):
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
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
    access = models.BooleanField(verbose_name='Доступ к маркету', default=False)

    def save(self, *args, **kwargs):
        self.last_login = datetime.datetime.now()
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


UserProfile = get_user_model()


class Subscription(models.Model):
    subscriber = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='subscriptions_made',
                                   verbose_name='Подписчик')
    subscribed_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='subscriptions_received',
                                      verbose_name='Подписан на')

    def __str__(self):
        return f'{self.subscriber} подписан на {self.subscribed_to}'


class Posts(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_posts',
                               verbose_name='Отправитель')
    poster = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_posts',
                               verbose_name='Получатель')
    text_post = models.CharField(max_length=6144, verbose_name='Текст поста')
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now=True)

