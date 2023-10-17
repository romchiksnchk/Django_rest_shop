from django.contrib.auth import logout, authenticate, login
from rest_framework import generics, filters, status, permissions, exceptions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Vacancies
from .serializers import UserIDSerializer, UserAllSerializer, LoginSerializer, RegisterSerializer,\
    VacanciesAllSerializer


class AllUserApiView(generics.ListCreateAPIView):
    """Все пользователи"""
    queryset = User.objects.all()
    serializer_class = UserAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    authentication_classes = (SessionAuthentication,)


class AllVacanciesApiView(generics.ListCreateAPIView):
    """Все пользователи"""
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    authentication_classes = (SessionAuthentication,)


class UserApiView(generics.RetrieveAPIView):
    """Пользователи по ID"""
    queryset = User.objects.all()
    serializer_class = UserIDSerializer
    authentication_classes = (SessionAuthentication,)


class RegisterAPI(generics.CreateAPIView):
    """ Регистрация"""
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class Logout(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        logout(request)
        return Response()


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                 raise exceptions.NotFound("Ничего не найдено")
        else:
            raise exceptions.NotFound("Ничего не найдено")