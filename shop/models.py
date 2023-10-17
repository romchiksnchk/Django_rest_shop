from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название магазина", unique=True)
    address = models.CharField(max_length=50, verbose_name="Адрес", unique=True)
    city = models.ManyToManyField('City', blank=False, verbose_name="Город")

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return f'{self.title}'


class City(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return f'{self.title}'
