from django.urls import path

from products.views import ShopListView, ProductListView
from .views import seller_dashboard, product_list

urlpatterns = [
    path('dashboard/', seller_dashboard, name='seller-dashboard'),
    path('list/', product_list, name='product-list'),
    path('shops/', ShopListView.as_view(), name='shop-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('', product_list, name='product-list'),
]
