from django.conf.urls import url
from shop.products.views.buy_product import BuyProduct
from shop.products.views.products import Products

urlpatterns = [
    url(r'buy/(?P<title>\w+)', view=BuyProduct.as_view()),
    url(r'(?P<option>\w+)', view=Products.as_view()),
    url('', view=Products.as_view())
]
