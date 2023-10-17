# Generated by Django 4.2.1 on 2023-10-17 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес доставки',
                'verbose_name_plural': 'Адреса доставки',
            },
        ),
        migrations.CreateModel(
            name='Obtain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Способ получения')),
            ],
            options={
                'verbose_name': 'Способ получения',
                'verbose_name_plural': 'Способы получения',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Метод оплаты',
                'verbose_name_plural': 'Методы оплаты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.deliveryaddress', verbose_name='Адрес доставки')),
                ('how_to_obtain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.obtain', verbose_name='Способ получения')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.paymentmethod', verbose_name='Метод оплаты')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
