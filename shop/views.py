from rest_framework import generics, filters, permissions
from rest_framework.response import Response
from .models import Shop, City
from .serializers import ShopAllSerializer, CityAllSerializer, ShopUpdateSerializer, \
    CityUpdateSerializer, ShopCreateSerializer, CityCreateSerializer


class AllShopApiView(generics.ListAPIView):
    """Все магазины"""
    queryset = Shop.objects.all()
    serializer_class = ShopAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address']
    permission_classes = (permissions.IsAuthenticated,)


class AllCityApiView(generics.ListAPIView):
    """Все магазины"""
    queryset = City.objects.all()
    serializer_class = CityAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class ShopApiView(generics.RetrieveAPIView):
    """Магазин по ID"""
    queryset = Shop.objects.all()
    serializer_class = ShopAllSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CityApiView(generics.RetrieveAPIView):
    """Город по ID"""
    queryset = City.objects.all()
    serializer_class = CityAllSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateShopApiView(generics.CreateAPIView):
    """Создание магазина"""
    serializer_class = ShopCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class CreateCityApiView(generics.CreateAPIView):
    """Создание города"""
    serializer_class = CityCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UpdateShopApiView(generics.UpdateAPIView):
    """Обновление магазина"""
    queryset = Shop.objects.all()
    serializer_class = ShopUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UpdateCityApiView(generics.UpdateAPIView):
    """Обновление города"""
    queryset = City.objects.all()
    serializer_class = CityUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)


class DeleteShopApiView(generics.DestroyAPIView):
    """Удаление магазина"""
    queryset = Shop.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление магазина успешно'})


class DeleteCityApiView(generics.DestroyAPIView):
    """Удаление города"""
    queryset = City.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление города успешно'})

