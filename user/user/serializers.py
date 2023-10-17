from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from .models import User, Vacancies
from .validators import MinimumLengthValidator
from rest_framework import serializers


class UserAllSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'images']


class VacanciesAllSerializer(ModelSerializer):

    class Meta:
        model = Vacancies
        fields = ['title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class UserIDSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['title', 'product', 'images']


class LoginSerializer(ModelSerializer):
    """ Сериалайзер для логина"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterSerializer(ModelSerializer):
    """ Сериалайзер для регистрации"""
    password = CharField(write_only=True, required=True)

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Пароль должен содержать минимум 8 символов")
        elif password.istitle() == False:
            raise serializers.ValidationError("Пароль должен содержать минимум 1 заглавную букву")
        return password

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'images', 'password']
