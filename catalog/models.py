from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import PositiveIntegerField
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', help_text="Введите название.")
    description = models.TextField(verbose_name='Описание', help_text="Введите описание.")
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=False,
        help_text="Введите цену в рублях.",
        verbose_name="Стоимость"
    )
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    views_counter = PositiveIntegerField(
        verbose_name="счётчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )
    author = models.ForeignKey(User, verbose_name="Автор курса", blank=True, null=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=100, verbose_name='Токен', null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'updated_at', 'category']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', help_text="Введите название.")
    description = models.TextField(verbose_name='Описание', help_text="Введите описание.")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version_name = models.CharField(max_length=100, verbose_name='Имя версии', help_text="Введите название.")
    version_number = models.CharField(max_length=50, verbose_name='Номер версии', help_text="Введите номер.")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.version_name} (v{self.version_number})"