from django.urls import path

from shop.views import HomePage, ProductDetail

urlpatterns = [
    path('product/<slug:slug>/', ProductDetail.as_view(), name='shop-product'),
    path('', HomePage.as_view(), name='shop-home'),
]
