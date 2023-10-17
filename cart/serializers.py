from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Cart


class UserCartSerializer(ModelSerializer):
    """Сериалайзер карзины"""

    class Meta:
        model = Cart
        fields = ['products', 'final_price']


class UpdateCartSerializer(ModelSerializer):
    """Сериалайзер изменения карзины"""
    final_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart
        fields = ['products', 'final_price']
