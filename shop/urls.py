from django.urls import path

from shop.views import HomePage, ProductDetail, CartPage

urlpatterns = [
    path('product/<slug:slug>/', ProductDetail.as_view(), name='shop-product'),
    path('cart', CartPage.as_view(), name='shop-cart'),
    path('', HomePage.as_view(), name='shop-home'),
]
