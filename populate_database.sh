#!/bin/sh

./manage.py migrate
./manage.py migrate --run-syncdb

./manage.py shell -c "
from shop.models import Product

Product.objects.filter().delete()

product = Product(title='apple', price=20, inventory_count=10)
product.save()

product = Product(title='orange', price=12, inventory_count=22)
product.save()

product = Product(title='pineapple', price=27, inventory_count=5)
product.save()

product = Product(title='iphone', price=500, inventory_count=0)
product.save()

"