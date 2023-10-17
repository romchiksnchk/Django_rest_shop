from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from shop.serializers import ShopVacanciesSerializer
from .models import Profile, Vacancies


class UserAllSerializer(ModelSerializer):
    """Сериалайзер всех пользователей"""

    class Meta:
        model = Profile
        fields = ['id', 'name', 'username', 'email', 'images', 'order']


class VacanciesAllSerializer(ModelSerializer):
    """Сериалайзер для вывода всех вакансий"""

    class Meta:
        model = Vacancies
        fields = ['id', 'title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class UserIDSerializer(ModelSerializer):
    """Сериалайзер вывода пользователя по ID"""

    class Meta:
        model = Profile
        fields = ['id', 'name', 'username', 'email', 'images', 'order']


class VacanciesIDSerializer(ModelSerializer):
    """Сериалайзер для вывода вакансий по ID"""
    shop = ShopVacanciesSerializer(many=True)

    class Meta:
        model = Vacancies
        fields = ['id', 'title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class UpdateUserSerializer(ModelSerializer):
    """Сериалайзер для изменения пользователя"""

    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'images']


class VacanciesUpdateSerializer(ModelSerializer):
    """Сериалайзер для обновления вакансий"""

    class Meta:
        model = Vacancies
        fields = ['id', 'title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class RegisterSerializer(ModelSerializer):
    """ Сериалайзер для регистрации"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'username', 'email', 'images', 'password']


class VacanciesCreateSerializer(ModelSerializer):
    """Сериалайзер для создание вакансии"""

    class Meta:
        model = Vacancies
        fields = '__all__'


class LoginSerializer(ModelSerializer):
    """Сериалайзер для логина"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['username', 'password']


class UserOrderSerializer(ModelSerializer):
    """Сериалайзер вывода данных пользователя в заказе"""

    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'cart']
