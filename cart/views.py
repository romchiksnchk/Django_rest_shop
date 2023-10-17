from rest_framework import generics
from cart.models import Cart
from cart.serializers import UpdateCartSerializer, UserCartSerializer
from core.permissions import IsUserOwner


class UserCartApiView(generics.RetrieveAPIView):
    """Карзина пользователя"""
    serializer_class = UserCartSerializer
    permission_classes = (IsUserOwner,)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class UpdateCartApiView(generics.UpdateAPIView):
    """Обновление пользователя"""
    queryset = Cart.objects.all()
    serializer_class = UpdateCartSerializer
    permission_classes = (IsUserOwner,)
