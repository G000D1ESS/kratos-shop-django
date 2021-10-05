import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .factories import ProductFactory

INCORRECT_DATA_ERRORS = (ValidationError, IntegrityError)


class TestProduct:

    def test_can_save_with_valid_data(self, transactional_db):
        ProductFactory()

    def test_can_not_save_with_negative_stock(self, transactional_db):
        with pytest.raises(INCORRECT_DATA_ERRORS):
            ProductFactory(stock=-1)

    def test_can_save_without_roundoff_if_price_with_two_decimal_places(self, transactional_db):
        float_price = 125.75
        product = ProductFactory(price=float_price)
        assert product.price == float_price

    def test_can_not_save_with_price_equal_zero(self, transactional_db):
        with pytest.raises(INCORRECT_DATA_ERRORS):
            ProductFactory(price=0)

    def test_can_not_save_with_price_lower_zero(self, transactional_db):
        with pytest.raises(INCORRECT_DATA_ERRORS):
            ProductFactory(price=-100)
