from django.urls import path
from .views import UpdateCartApiView, UserCartApiView

app_name = "cart"

urlpatterns = [
    path('user-cart<int:pk>/', UserCartApiView.as_view()),
    path('cart-update<int:pk>/', UpdateCartApiView.as_view())
]
