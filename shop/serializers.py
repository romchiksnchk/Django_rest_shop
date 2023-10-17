from rest_framework.serializers import ModelSerializer
from .models import Shop, City


class ShopAllSerializer(ModelSerializer):
    """Сериалайзер всех магазинов"""

    class Meta:
        model = Shop
        fields = ['title', 'address', 'city']


class CityAllSerializer(ModelSerializer):
    """Сериалайзер всех городов"""

    class Meta:
        model = City
        fields = ['title']


class ShopCreateSerializer(ModelSerializer):
    """Сериалайзер создания магазинов"""

    class Meta:
        model = Shop
        fields = '__all__'


class CityCreateSerializer(ModelSerializer):
    """Сериалайзер создания городов"""

    class Meta:
        model = City
        fields = '__all__'


class ShopUpdateSerializer(ModelSerializer):
    """Сериалайзер обновления магазинов"""

    class Meta:
        model = Shop
        fields = '__all__'


class CityUpdateSerializer(ModelSerializer):
    """Сериалайзер обновления городов"""

    class Meta:
        model = City
        fields = '__all__'


class ShopVacanciesSerializer(ModelSerializer):
    """Сериалайзер для вывода города в сериалайзере вакансий"""
    city = CityAllSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['title', 'address', 'city']
