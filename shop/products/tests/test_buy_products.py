import pytest
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
        banana = list(Product.objects.filter(title='banana'))[0]
        self.assertEqual(banana.inventory_count, 14)