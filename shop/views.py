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
                'id': product.id,
                'main_image': product.images.first(),
            }
            context['products'].append(data)
        return context

class CartPage(TemplateView):
    """ Cart page view """
    template_name = 'shop/cart.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(session=request.session, **kwargs)
        return self.render_to_response(context)

    def get_context_data(self, session, **kwargs):
        context = {
            'products': [],
        }
        products = session.get('products', [])
        for product_id in products:
            product = Product.objects.get(id=product_id)
            context['products'].append(product)
        return context

class ProductDetail(DetailView):

    model = Product
