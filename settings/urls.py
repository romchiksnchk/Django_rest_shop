from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product.urls', namespace='product')),
    path('api/', include('user.urls', namespace='user')),
    path('api/', include('shop.urls', namespace='shop')),
    path('api/', include('cart.urls', namespace='cart')),
    path('api/', include('order.urls', namespace='order'))
]
