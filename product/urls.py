from django.urls import path
from .views import AllProductApiView, AllCategoryApiView, CategoryApiView, SaleProductApiView, \
    CreateCommentApiView, CreateProductApiView, ProductApiView, AllCommentApiView, \
    UpdateProductApiView, UpdateCategoryApiView, UpdateCommentApiView, CommentIDApiView, \
    DeleteProductApiVew, CreateCategoryApiView, DeleteCategoryApiVew, DeleteCommentApiVew

app_name = "product"

urlpatterns = [
    path('all-products/', AllProductApiView.as_view()),
    path('all-category/', AllCategoryApiView.as_view()),
    path('all-comments/', AllCommentApiView.as_view()),
    path('products<int:pk>/', ProductApiView.as_view()),
    path('category<int:pk>/', CategoryApiView.as_view()),
    path('comments<int:pk>/', CommentIDApiView.as_view()),
    path('create-products/', CreateProductApiView.as_view()),
    path('category-create/', CreateCategoryApiView.as_view()),
    path('create-comment/', CreateCommentApiView.as_view()),
    path('delete-products<int:pk>/', DeleteProductApiVew.as_view()),
    path('products-update<int:pk>/', UpdateProductApiView.as_view()),
    path('category-update<int:pk>/', UpdateCategoryApiView.as_view()),
    path('comments-update<int:pk>/', UpdateCommentApiView.as_view()),
    path('products-update<int:pk>/', UpdateProductApiView.as_view()),
    path('category-delete<int:pk>/', DeleteCategoryApiVew.as_view()),
    path('delete-comment<int:pk>/', DeleteCommentApiVew.as_view()),
    path('sale-products/', SaleProductApiView.as_view()),
]
