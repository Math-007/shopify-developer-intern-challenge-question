import pytest
from django.http import HttpResponseNotFound
from django.test import TestCase
from django.utils.encoding import force_text
from shop.models import Product


@pytest.mark.django_db
class TestBuyProduct(TestCase):

    expected_json_buy_apple = {
        'price': 20, 'title': 'banana', 'inventory_count': 14
    }

    def setUp(self):
        Product.objects.create(
            inventory_count=15, price=20.0, title="banana"
        )
        Product.objects.create(
            inventory_count=0, price=15.0, title="apple"
        )

    def test_buy_product(self):
        response = self.client.delete('/shop/products/buy/banana')
        self.assertJSONEqual(force_text(response.content), self.expected_json_buy_apple)
        banana = Product.objects.get(title='banana')
        self.assertEqual(banana.inventory_count, 14)

    def test_buy_not_found_product(self):
        response = self.client.delete('/shop/products/buy/itemdoesnotexist')
        self.assertJSONEqual(force_text(response.content), {"Item not found": "itemdoesnotexist"})
        self.assertEqual(response.status_code, HttpResponseNotFound.status_code)
