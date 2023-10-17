from django.contrib import admin
from .models import Shop, City


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
