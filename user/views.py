from rest_framework import generics, filters, permissions
from rest_framework.response import Response
from core.permissions import IsUserUpdate
from .models import Profile, Vacancies
from .serializers import UserIDSerializer, UserAllSerializer, RegisterSerializer, \
    VacanciesAllSerializer, VacanciesIDSerializer, UpdateUserSerializer, VacanciesUpdateSerializer, \
    VacanciesCreateSerializer


class AllUserApiView(generics.ListCreateAPIView):
    """Все пользователи"""
    queryset = Profile.objects.all()
    serializer_class = UserAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = (permissions.IsAuthenticated,)


class AllVacanciesApiView(generics.ListCreateAPIView):
    """Все вакансии"""
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class UserApiView(generics.RetrieveAPIView):
    """Пользователи по ID"""
    queryset = Profile.objects.all()
    serializer_class = UserIDSerializer
    permission_classes = (permissions.IsAuthenticated,)


class VacanciesIDView(generics.RetrieveAPIView):
    """Вакансии по ID"""
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesIDSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RegisterAPI(generics.CreateAPIView):
    """ Регистрация"""
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class CreateVacanciesApiView(generics.CreateAPIView):
    """Создание вакансии"""
    serializer_class = VacanciesCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UpdateUserAPI(generics.UpdateAPIView):
    """Обновление пользователя"""
    queryset = Profile.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsUserUpdate,)


class UpdateVacanciesAPI(generics.UpdateAPIView):
    """Обновление вакансий"""
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)


class DeleteUserApiView(generics.DestroyAPIView):
    """Удаление пользователя"""
    queryset = Profile.objects.all()
    permission_classes = (IsUserUpdate,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление пользователя успешно'})


class DeleteVacanciesApiVew(generics.DestroyAPIView):
    """Удаление вакансии"""
    queryset = Vacancies.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление вакансии успешно'})


# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer
#
#     def post(self, request, format=None):
#         data = request.data
#         username = data.get('username', None)
#         password = data.get('password', None)
#         user = authenticate(username=username, password=password)
#         if user is None:
#             raise exceptions.NotFound("Такого пользователя не существует")
#         if not user.check_password(password):
#             raise exceptions.NotFound("Не верный логин или пароль")
#         else:
#             login(request, user)
#             refresh = RefreshToken.for_user(user)
#             return Response({'access_token': str(refresh.access_token), 'refresh_token': str(
#                 refresh)})
