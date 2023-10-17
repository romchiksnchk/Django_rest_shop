from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView
from .views import AllUserApiView, UserApiView, RegisterAPI, \
    AllVacanciesApiView, VacanciesIDView, UpdateUserAPI, UpdateVacanciesAPI, DeleteUserApiView, \
    DeleteVacanciesApiVew, CreateVacanciesApiView

app_name = "product"

urlpatterns = [
    path('all-user/', AllUserApiView.as_view()),
    path('all-vacancies/', AllVacanciesApiView.as_view()),
    path('user<int:pk>/', UserApiView.as_view()),
    path('vacancies<int:pk>/', VacanciesIDView.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('vacancies-create/', CreateVacanciesApiView.as_view()),
    path('user-update<int:pk>/', UpdateUserAPI.as_view()),
    path('vacancies-update<int:pk>/', UpdateVacanciesAPI.as_view()),
    path('user-delete<int:pk>/', DeleteUserApiView.as_view()),
    path('vacancies-delete<int:pk>/', DeleteVacanciesApiVew.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
