from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone_number = models.CharField(max_length=10, verbose_name='номер телефона', blank=True, null=True, help_text='Введите номер телефона')
    city = models.CharField(max_length=30, verbose_name='имя пользователя', blank=True, null=True, help_text='Введите имя пользователя')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, help_text='Выберите аватар'),
    token = models.CharField(max_length=100, verbose_name='Токен', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


