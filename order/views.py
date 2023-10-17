from rest_framework import generics, filters, permissions
from rest_framework.response import Response
from core.permissions import IsUserOwner
from .models import Order, Obtain, DeliveryAddress, PaymentMethod
from .serializers import OrderAllSerializer, ObtainAllSerializer, DeliveryAddressAllSerializer, \
    PaymentMethodAllSerializer, OrderCreateSerializer, ObtainCreateSerializer, \
    DeliveryAddressCreateSerializer, PaymentMethodCreateSerializer, OrderUpdateSerializer, \
    ObtainUpdateSerializer, \
    DeliveryAddressUpdateSerializer, PaymentMethodUpdateSerializer, OrderIDSerializer


class AllOrderApiView(generics.ListAPIView):
    """Все заказы"""
    queryset = Order.objects.all()
    serializer_class = OrderAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']
    permission_classes = (permissions.IsAdminUser,)


class UserAllOrderApiView(generics.ListAPIView):
    """Заказы пользователя"""
    serializer_class = OrderIDSerializer
    permission_classes = (IsUserOwner,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class AllObtainApiView(generics.ListAPIView):
    """Все способы доставки"""
    queryset = Obtain.objects.all()
    serializer_class = ObtainAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAdminUser,)


class AllDeliveryAddressApiView(generics.ListAPIView):
    """Все адреса доставки"""
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city__title', 'address']
    permission_classes = (permissions.IsAdminUser,)


class AllPaymentMethodApiView(generics.ListAPIView):
    """Все способы оплаты"""
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAdminUser,)


class OrderIDApiView(generics.RetrieveAPIView):
    """Заказ по ID"""
    queryset = Order.objects.all()
    serializer_class = OrderIDSerializer
    permission_classes = (IsUserOwner,)


class CreateOrderApiView(generics.CreateAPIView):
    """Создать заказ"""
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateObtainApiView(generics.CreateAPIView):
    """Создать способ отправки"""
    serializer_class = ObtainCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class CreateDeliveryAddressApiView(generics.CreateAPIView):
    """Создать адрес доставки"""
    serializer_class = DeliveryAddressCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class CreatePaymentMethodApiView(generics.CreateAPIView):
    """Создать способ оплаты"""
    serializer_class = PaymentMethodCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UpdateOrderApiView(generics.UpdateAPIView):
    """Обновить заказ"""
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UpdateObtainApiView(generics.UpdateAPIView):
    """Обновить способ получения"""
    queryset = Obtain.objects.all()
    serializer_class = ObtainUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UpdateDeliveryAddressApiView(generics.UpdateAPIView):
    """Обновить адрес доставки"""
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UpdatePaymentMethodApiView(generics.UpdateAPIView):
    """Обновить способ оплаты"""
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)


class OrderDeleteApiView(generics.DestroyAPIView):
    """ Удаление заказа """
    queryset = Order.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление заказа успешно'})


class ObtainDeleteApiView(generics.DestroyAPIView):
    """ Удаление способа получения """
    queryset = Obtain.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление способа получения успешно'})


class DeliveryAddressDeleteApiView(generics.DestroyAPIView):
    """ Удаление адреса доставки """
    queryset = DeliveryAddress.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление адреса доставки успешно'})


class PaymentMethodDeleteApiView(generics.DestroyAPIView):
    """ Удаление способа оплаты"""
    queryset = PaymentMethod.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление способа оплаты успешно'})
