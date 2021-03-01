from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ProductViewSet, CartView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'product', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('cart', CartView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
