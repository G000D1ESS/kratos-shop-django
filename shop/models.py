from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

from kratos.mixins import ValidateOnSaveMixin


def number_greater_than_zero(value):
    if value <= 0:
        raise ValidationError(
            '%(value)s number is lower or equal zero an',
            params={'value': value},
        )


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=30)
    products = models.ManyToManyField('Product', blank=True)
    available = models.BooleanField(default=True, blank=True)

    @property
    def is_available(self):
        return self.available

    def __str__(self):
        return self.name

    class Meta:
        pass


class Product(ValidateOnSaveMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    slug = models.SlugField(unique=True)
    sku = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=512)
    stock = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, validators=[number_greater_than_zero])
    images = models.ManyToManyField('Image', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def is_available(self):
        return (self.stock > 0) & self.available

    def show_price(self):
        return f'{self.price} ₽'
    show_price.short_description = 'Цена'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created', 'name']


class Image(models.Model):
    image = models.ImageField(upload_to='img')

    @property
    def url(self):
        return self.image.url

    def __str__(self):
        return self.url

    class Meta:
        pass
