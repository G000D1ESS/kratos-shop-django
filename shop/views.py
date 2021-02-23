from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from shop.models import Product


class HomePage(TemplateView):
    """ Home page view"""
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = {'products': []}
        for product in Product.objects.all():
            data = {
                'name': product.name,
                'main_image': product.images.first(),
            }
            context['products'].append(data)
        return context


class ProductDetail(DetailView):

    model = Product
