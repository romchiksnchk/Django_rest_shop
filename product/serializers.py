from rest_framework.serializers import ModelSerializer
from .models import Product, Category, Comment


class ProductAllSerializer(ModelSerializer):
    """Сериалайзер всех товаров"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image', 'price', 'category']


class ProductSaleSerializer(ModelSerializer):
    """Сериалайзер товаров по скидке"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image', 'price', 'price_discount']


class CategoryAllSerializer(ModelSerializer):
    """Сериалайзер всех категорий"""

    class Meta:
        model = Category
        fields = ['id', 'title', 'products']


class CommentAllSerializer(ModelSerializer):
    """Сериалайзер всех комментарией"""

    class Meta:
        model = Comment
        fields = ['id', 'title', 'description', 'user', 'rating', 'products']


class ProductIDSerializer(ModelSerializer):
    """Сериалайзер товаров пo ID"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image', 'price', 'category', 'comment']


class CategoryIDSerializer(ModelSerializer):
    """Сериалайзер категорий пo ID"""

    class Meta:
        model = Category
        fields = ['id', 'title', 'products']


class CommentIDSerializer(ModelSerializer):
    """Сериалайзер комментариев пo ID"""

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'user', 'rating', 'products']


class ProductCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания продукции"""

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'image', 'price', 'sale', 'discount']


class CategoryCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания категорий"""

    class Meta:
        model = Category
        fields = '__all__'


class CommentCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания комментария"""

    class Meta:
        model = Comment
        fields = ['title', 'description', 'rating', 'products']


class ProductUpdateSerializer(ModelSerializer):
    """Сериалайзер для создания товаров"""

    class Meta:
        model = Product
        fields = '__all__'


class CategoryUpdateSerializer(ModelSerializer):
    """Сериалайзер для создания категорий"""

    class Meta:
        model = Category
        fields = '__all__'


class CommentUpdateSerializer(ModelSerializer):
    """Сериалайзер для создания комментариев"""

    class Meta:
        model = Comment
        fields = ['title', 'description', 'rating']
