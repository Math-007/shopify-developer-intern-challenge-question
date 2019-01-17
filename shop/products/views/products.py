from django.views.generic import View
from django.http import JsonResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Product


class Products(View):

    def get(self, request, option="all"):
        if option == "all":
            return self._get_all_products()
        elif option == "available":
            return self._get_available_products()
        else:
            return self._get_specific_product(option)

    def _get_all_products(self):
        list_product = list(Product.objects.all())
        json = self._products_to_json(list_product)
        return JsonResponse(json)

    def _get_available_products(self):
        list_product = list(Product.objects.filter(inventory_count__gt=0))
        json = self._products_to_json(list_product)
        return JsonResponse(json)

    def _get_specific_product(self, title):
        try :
            specific_product = Product.objects.get(title=title)
        except ObjectDoesNotExist:
            return JsonResponse(self._product_not_found_to_json(title), status=HttpResponseNotFound.status_code)

        return JsonResponse(self._to_product_json(specific_product.to_json()))

    def _products_to_json(self, list_products):
        list_json = list(map(lambda x: x.to_json(), list_products))
        return self._to_product_json(list_json)

    def _to_product_json(self, object):
        if isinstance(object, list):
            return {"products": object}
        else:
            return {"product": object}

    def _product_not_found_to_json(self, product_title):
        return {"Item not found": product_title}

