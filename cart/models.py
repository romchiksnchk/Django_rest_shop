from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import user.models
from product.models import Product


class Cart(models.Model):
    """Модель корзины"""
    title = models.CharField(max_length=50, default='Корзина', editable=False,
                             verbose_name='Корзина')
    products = models.ManyToManyField(Product, blank=True, verbose_name='Товары')
    user = models.OneToOneField('user.Profile', on_delete=models.CASCADE, related_name='cart',
                                  verbose_name='Пользователь')
    final_price = models.IntegerField(default=0, verbose_name='Цена')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    @receiver(post_save, sender='user.Profile', dispatch_uid="create_cart_user")
    def create_cart(sender, instance, created, **kwargs):
        if created:
            Cart.objects.create(user=instance)
        instance.cart.save()

    def __str__(self) -> str:
        return f'{self.title} - {self.user.username}'
