from django.views.generic import View
from django.http import JsonResponse, HttpResponseNotFound
from shop.models import Product


class BuyProduct(View):

    def delete(self, request, title=None):
        product = Product.objects.get(title=title)
        if not product:
            return JsonResponse({
                "Error": "Product {} does not exist".format(title)
            }, status=HttpResponseNotFound.status_code)

        if product.inventory_count <= 0:
            return JsonResponse({
                "Error": "Product {} has no inventory left".format(title)
            }, status=HttpResponseNotFound.status_code)

        product.inventory_count -= 1
        product.save()

        return JsonResponse(product.to_json())

