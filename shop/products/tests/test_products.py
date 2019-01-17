from django.test import TestCase
from django.utils.encoding import force_text

from shop.models import Product
import pytest


@pytest.mark.django_db
class ProductsTest(TestCase):
    expected_json_all = {'products':
        [
            {'inventory_count': 15, 'price': 20, 'title': 'banana'},
            {'inventory_count': 0, 'price': 15, 'title': 'apple'}
        ]
    }

    expected_json_available = {'products':
        [
            {'inventory_count': 15, 'price': 20, 'title': 'banana'}
        ]
    }

    expected_json_bad_request = {
        "Choices are": [
            "all",
            "available"
        ]
    }

    expected_json_get_specific_product = {
        "product":
            {'inventory_count': 0, 'price': 15, 'title': 'apple'}

    }

    def setUp(self):
        Product.objects.create(
            inventory_count=15, price=20.0, title="banana"
        )
        Product.objects.create(
            inventory_count=0, price=15.0, title="apple"
        )

    def test_get_products_all(self):
        response = self.client.get('/shop/products')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(force_text(response.content), self.expected_json_all)

    def test_get_products_available(self):
        response = self.client.get('/shop/products/available')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(force_text(response.content), self.expected_json_available)

    def test_get_specific_product(self):
        response = self.client.get("/shop/products/apple")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(force_text(response.content), self.expected_json_get_specific_product)

    def test_get_not_existing_product(self):
        response = self.client.get('/shop/products/thisproductdoesnotexitst')
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(force_text(response.content), {"Item not found": "thisproductdoesnotexitst"})
