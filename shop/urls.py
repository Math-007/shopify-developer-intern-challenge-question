from django.conf.urls import url, include

urlpatterns = [
    url(r'products', include('shop.products.urls'))
]