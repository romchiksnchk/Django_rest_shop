from django.urls import path
from .views import AllUserApiView, UserApiView, LoginAPIView, RegisterAPI, Logout, AllVacanciesApiView

app_name = "product"

urlpatterns = [
    path('all-user/', AllUserApiView.as_view()),
    path('all-vacancies/', AllVacanciesApiView.as_view()),
    path('user<int:pk>/', UserApiView.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', Logout.as_view()),
]
