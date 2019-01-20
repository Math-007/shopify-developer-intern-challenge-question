# shopify developper intern challenge question
see https://docs.google.com/document/d/1J49NAOIoWYOumaoQCKopPfudWI_jsQWVKlXmw1f1r-4/edit for details

The API was built using the python framework django

A Dockerfile is provided to start the server and run the unit tests

## Enter the docker container

```
$ docker build --tag=shopify -f Dockerfile.shopify .
$ docker run -p 8000:8000 -it shopify:latest
```

## Once in the docker container 

* Start server
```
(/home/root/shopify) $ ./manage.py runserver 0.0.0.0:8000
```

* Run unittests
```
(/home/root/shopify) $ pytest
```

* Initialize the database with a few products
```
(/home/root/shopify) $ ./populate_database.sh
```

## Usage

* Get available products

curl --request GET \
  --url http://localhost:8000/shop/products/available

* Get all products

curl --request GET \
  --url http://localhost:8000/shop/products/

* Get information of a specific product (ex: apple)

curl --request GET \
  --url http://localhost:8000/shop/products/apple

* Buy a product (ex: apple)
 
curl --request DELETE \
  --url http://localhost:8000/shop/products/buy/apple