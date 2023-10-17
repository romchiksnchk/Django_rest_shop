from django.db import models
from cart.models import Cart
from shop.models import City
from user.models import Profile


class Order(models.Model):
    """Модель заказа"""
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Заказчик',
                             related_name='order')
    how_to_obtain = models.ForeignKey('Obtain', on_delete=models.CASCADE, null=False, blank=False,
                                      verbose_name='Способ получения')
    delivery_address = models.ForeignKey('DeliveryAddress', on_delete=models.CASCADE, null=False,
                                         blank=False, verbose_name='Адрес доставки')
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, null=False,
                                       blank=False, verbose_name='Метод оплаты')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f'{self.user} - {self.delivery_address}'


class Obtain(models.Model):
    """Модель способа получения"""
    title = models.CharField(max_length=50, verbose_name='Способ получения', unique=True)

    class Meta:
        verbose_name = 'Способ получения'
        verbose_name_plural = 'Способы получения'

    def __str__(self) -> str:
        return f'{self.title}'


class DeliveryAddress(models.Model):
    """Модель адреса доставки"""
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False,
                             verbose_name='Город')
    address = models.CharField(max_length=150, verbose_name='Адрес', unique=True)

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'

    def __str__(self) -> str:
        return f'{self.city} - {self.address}'


class PaymentMethod(models.Model):
    """Модель способа оплаты"""
    title = models.CharField(max_length=50, verbose_name='Название', unique=True)
    description = models.CharField(max_length=150, null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Метод оплаты'
        verbose_name_plural = 'Методы оплаты'

    def __str__(self) -> str:
        return f'{self.title}'
