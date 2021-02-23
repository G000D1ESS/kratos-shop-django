from django.urls import path

from shop.views import ProductDetail

urlpatterns = [
    path('<slug:slug>/', ProductDetail.as_view(), name='prodcut-detail')
]