from rest_framework import generics, filters, permissions
from rest_framework.response import Response
from core.permissions import IsUserUpdate
from .models import Product, Category, Comment
from .serializers import ProductAllSerializer, CategoryAllSerializer, ProductIDSerializer, \
    ProductSaleSerializer, CommentCreateSerializer, ProductCreateSerializer, CategoryIDSerializer, \
    CommentAllSerializer, ProductUpdateSerializer, CategoryUpdateSerializer, \
    CommentUpdateSerializer, CategoryCreateSerializer


class AllProductApiView(generics.ListCreateAPIView):
    """Вся продукция"""
    queryset = Product.objects.all()
    serializer_class = ProductAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class ProductApiView(generics.RetrieveAPIView):
    """Продукция по ID"""
    queryset = Product.objects.all()
    serializer_class = ProductIDSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SaleProductApiView(generics.ListCreateAPIView):
    """Продукция по скидке"""
    queryset = Product.objects.filter(sale=True)
    serializer_class = ProductSaleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class AllCategoryApiView(generics.ListCreateAPIView):
    """Все категории"""
    queryset = Category.objects.all()
    serializer_class = CategoryAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class CategoryApiView(generics.RetrieveAPIView):
    """Категории по ID"""
    queryset = Category.objects.all()
    serializer_class = CategoryIDSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AllCommentApiView(generics.ListCreateAPIView):
    """Все комментарии"""
    queryset = Comment.objects.all()
    serializer_class = CommentAllSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CommentIDApiView(generics.RetrieveAPIView):
    """Комментарий по ID"""
    queryset = Comment.objects.all()
    serializer_class = CategoryIDSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateProductApiView(generics.CreateAPIView):
    """Создание товара"""
    serializer_class = ProductCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class CreateCategoryApiView(generics.CreateAPIView):
    """Создание категории"""
    serializer_class = CategoryCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class CreateCommentApiView(generics.CreateAPIView):
    """Создание коментария"""
    serializer_class = CommentCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateProductApiView(generics.UpdateAPIView):
    """Обновление товара"""
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)


class UpdateCategoryApiView(generics.UpdateAPIView):
    """Обновление категории"""
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    permissions_classes = (permissions.IsAdminUser,)


class UpdateCommentApiView(generics.UpdateAPIView):
    """Обновление комментария"""
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permissions_classes = (IsUserUpdate,)


class DeleteProductApiVew(generics.DestroyAPIView):
    """Удаление товара"""
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление товара успешно'})


class DeleteCategoryApiVew(generics.DestroyAPIView):
    """Удаление категории"""
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление категории успешно'})


class DeleteCommentApiVew(generics.DestroyAPIView):
    """Удаление комментария"""
    queryset = Comment.objects.all()
    permission_classes = (IsUserUpdate,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление коментария успешно'})
