from django.contrib import admin
from .models import Product, Category, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['price_discount']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
