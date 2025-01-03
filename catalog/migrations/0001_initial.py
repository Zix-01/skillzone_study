# Generated by Django 5.1 on 2024-08-27 10:26

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название.', max_length=100, verbose_name='Имя')),
                ('description', models.TextField(help_text='Введите описание.', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название.', max_length=100, verbose_name='Имя')),
                ('description', models.TextField(help_text='Введите описание.', verbose_name='Описание')),
                ('image', models.ImageField(help_text='Загрузите изображение продукта.', upload_to='product/photo', verbose_name='Фото')),
                ('price', models.IntegerField(help_text='Введите цену в рублях.', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Стоимость')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'price', 'created_at', 'updated_at', 'category'],
            },
        ),
    ]
