from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from shop.models import Shop, City


class Profile(AbstractUser):
    name = models.CharField(max_length=35, null=False, blank=False, verbose_name='Имя')
    username = models.CharField(max_length=25, verbose_name="имя пользователя", unique=True)
    email = models.EmailField(null=False, blank=False, verbose_name="Почта", unique=True)

    images = models.ImageField(upload_to="image/user/", null=False, blank=False,
                               verbose_name="Картинка")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.username}'


class Vacancies(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название вакансии", unique=True)
    Responsibilities = models.CharField(max_length=200, verbose_name="Обязанности")
    Requirements = models.CharField(max_length=200, verbose_name="Требования")
    Conditions = models.CharField(max_length=200, verbose_name="Условности")
    price = models.IntegerField(default=0, verbose_name='Оплата', null=False, blank=False)
    shop = models.ManyToManyField(Shop, verbose_name="Адрес магазина", blank=False)

    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f'{self.title}'

