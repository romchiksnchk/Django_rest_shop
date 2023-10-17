from django.contrib import admin
from .models import Order, Obtain, DeliveryAddress, PaymentMethod


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Obtain)
class ObtainAdmin(admin.ModelAdmin):
    pass


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass
