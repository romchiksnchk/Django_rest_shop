from django.urls import path
from .views import AllShopApiView, ShopApiView, CityApiView, AllCityApiView, UpdateShopApiView, \
    UpdateCityApiView, DeleteShopApiView, DeleteCityApiView, CreateShopApiView, CreateCityApiView

app_name = "shop"

urlpatterns = [
    path('all-shop/', AllShopApiView.as_view()),
    path('all-city/', AllCityApiView.as_view()),
    path('shop<int:pk>/', ShopApiView.as_view()),
    path('city<int:pk>/', CityApiView.as_view()),
    path('shop-create/', CreateShopApiView.as_view()),
    path('city-create/', CreateCityApiView.as_view()),
    path('shop-update<int:pk>/', UpdateShopApiView.as_view()),
    path('city-update<int:pk>/', UpdateCityApiView.as_view()),
    path('shop-delete<int:pk>/', DeleteShopApiView.as_view()),
    path('city-delete<int:pk>/', DeleteCityApiView.as_view()),
]
