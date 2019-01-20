## shopify-developper-intern-challend-question
see https://docs.google.com/document/d/1J49NAOIoWYOumaoQCKopPfudWI_jsQWVKlXmw1f1r-4/edit for details

The API was built using the python framwork django

A Dockerfile is provided to run the server and its unittest

## Enter the docker container

```
(shopify) $ docker build --tag=shopify -f Dockerfile.shopify .
(shopify) $ docker run -p 8000:8000 -it shopify:latest
```

## Once in the docker container 

* Run server
```
(/home/root/shopify) $ ./manage.py runserver 0.0.0.0:8000
```

* Run unittests
```
(/home/root/shopify) $ pytest
```

## Usage

* Get available products

curl --request GET \
  --url http://localhost:8000/shop/products/available

* Get all products

curl --request GET \
  --url http://localhost:8000/shop/products/

* Get information of a specific product 

curl --request GET \
  --url http://localhost:8000/shop/products/<title>

* Buy a product

curl --request DELETE \
  --url http://localhost:8000/shop/products/buy/apple


