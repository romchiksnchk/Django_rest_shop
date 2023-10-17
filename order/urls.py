from django.urls import path
from .views import AllOrderApiView, AllObtainApiView, AllDeliveryAddressApiView, \
    AllPaymentMethodApiView, CreateOrderApiView, CreateObtainApiView, CreateDeliveryAddressApiView, \
    CreatePaymentMethodApiView, UpdateOrderApiView, UpdateObtainApiView, \
    UpdateDeliveryAddressApiView, \
    UpdatePaymentMethodApiView, OrderDeleteApiView, ObtainDeleteApiView, \
    DeliveryAddressDeleteApiView, \
    PaymentMethodDeleteApiView, UserAllOrderApiView, OrderIDApiView

app_name = "order"

urlpatterns = [
    path('all-order/', AllOrderApiView.as_view()),
    path('all-user-order/', UserAllOrderApiView.as_view()),
    path('all-obtain/', AllObtainApiView.as_view()),
    path('all-delivery-address/', AllDeliveryAddressApiView.as_view()),
    path('all-payment-method/', AllPaymentMethodApiView.as_view()),
    path('user-order<int:pk>', OrderIDApiView.as_view()),
    path('order-create/', CreateOrderApiView.as_view()),
    path('obtain-create/', CreateObtainApiView.as_view()),
    path('delivery-address-create/', CreateDeliveryAddressApiView.as_view()),
    path('payment-method-create/', CreatePaymentMethodApiView.as_view()),
    path('order-update<int:pk>/', UpdateOrderApiView.as_view()),
    path('obtain-update<int:pk>/', UpdateObtainApiView.as_view()),
    path('delivery-address-update<int:pk>/', UpdateDeliveryAddressApiView.as_view()),
    path('payment-method-update<int:pk>/', UpdatePaymentMethodApiView.as_view()),
    path('order-delete<int:pk>/', OrderDeleteApiView.as_view()),
    path('obtain-delete<int:pk>/', ObtainDeleteApiView.as_view()),
    path('delivery-address-delete<int:pk>/', DeliveryAddressDeleteApiView.as_view()),
    path('payment-method-delete<int:pk>/', PaymentMethodDeleteApiView.as_view()),
]
