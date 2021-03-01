from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, AllowAny

from kratos.tasks import send_offer

from api.serializers import UserSerializer, ProductSerializer
from shop.models import Product


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        print(request.session)
        content = {'user_session': request.session}
        return Response(content)

    def post(self, request, format=None):
        products = request.session.get('products', [])
        if 'add_to_cart' in request.POST:
            product = request.POST['add_to_cart']
            products.append(product)
            request.session['products'] = products
        else:
            product = {}
        content = {
            'data': request.POST,
            'products': products,
            'add_to_cart': product,
        }
        return Response(content)

    def put(self, request, format=None):
        offer = []
        products = request.session.get('products', [])
        for product_id in products:
            product = Product.objects.get(id=product_id)
            offer_data = {
                'name': product.name,
                'price': product.price,
            }
            offer.append(offer_data)
        send_offer.delay(offer)
        request.session['products'] = []
        return Response({'status': 'success'})
