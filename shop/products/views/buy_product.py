from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.http import JsonResponse, HttpResponseNotFound
from shop.models import Product


class BuyProduct(View):

    def delete(self, request, title=None):
        try:
            product = Product.objects.get(title=title)
        except ObjectDoesNotExist:
            return JsonResponse(self._product_not_found_to_json(title), status=HttpResponseNotFound.status_code)

        if product.inventory_count <= 0:
            return JsonResponse({
                "Error": "Product {} has no inventory left".format(title)
            }, status=HttpResponseNotFound.status_code)

        product.inventory_count -= 1
        product.save()

        return JsonResponse(product.to_json())

    def _product_not_found_to_json(self, product_title):
        return {"Item not found": product_title}
