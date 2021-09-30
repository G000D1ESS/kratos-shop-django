from django.contrib import admin
from django.urls import path, include

from api import urls as api_urls
from shop import urls as shop_urls

urlpatterns = [
    path('', include(shop_urls)),
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
