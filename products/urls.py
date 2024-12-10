from django.urls import path
from .views import ShopListView, ProductListView

urlpatterns = [
    path('shops/', ShopListView.as_view(), name='shop-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
]
