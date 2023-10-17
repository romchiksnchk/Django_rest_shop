# Generated by Django 4.2.1 on 2023-10-17 09:28

import django.core.validators
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
                ('title', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.CharField(max_length=260, verbose_name='Текст комментария')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, verbose_name='оценка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Товар')),
                ('description', models.CharField(max_length=260, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image/product/', verbose_name='Картинка')),
                ('price', models.IntegerField(default=1000, verbose_name='Цена')),
                ('sale', models.BooleanField(default=False, verbose_name='Скидка')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Скидка в процентах')),
                ('price_discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Цена с скидкой')),
                ('category', models.ManyToManyField(related_name='products', to='product.category', verbose_name='Категория')),
                ('comment', models.ManyToManyField(blank=True, related_name='products', to='product.comment', verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]