from django.contrib.auth.models import AbstractUser
from django.db import models
from shop.models import Shop
from django.core.validators import RegexValidator
from .validators import MinimumLengthValidator


class User(AbstractUser):
    username = models.CharField(max_length=20, verbose_name="Никнейм", unique=True,)
    email = models.EmailField(null=False, blank=False, verbose_name="Почта")
    images = models.ImageField(upload_to="image/user/", null=False, blank=False, verbose_name="Картинка")
    password = models.CharField(max_length=15, verbose_name="Пароль", validators=[MinimumLengthValidator])
    # USERNAME_FIELD = 'email'

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
    shop = models.ManyToManyField(Shop, null=False, verbose_name="Адрес магазина")

    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f'{self.title}'

