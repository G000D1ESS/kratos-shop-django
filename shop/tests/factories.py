import datetime

import factory

from shop import models


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Image

    image = factory.django.ImageField()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    slug = factory.Faker('slug')
    sku = factory.Faker('ean8')
    name = factory.Faker('sentence', nb_words=3)
    stock = factory.Faker('pyint', min_value=1, max_value=255)
    available = True
    price = factory.Faker('pyint', min_value=1, max_value=49999)
    created = factory.LazyAttribute(lambda _: datetime.datetime.now())

    @factory.post_generation
    def images(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.images.add(*extracted)
