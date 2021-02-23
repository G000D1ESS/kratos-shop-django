from django.utils import timezone
from django.views.generic.detail import DetailView

from shop.models import Product


class ProductDetail(DetailView):

    model = Product