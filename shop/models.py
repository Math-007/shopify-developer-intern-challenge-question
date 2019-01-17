from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=75)
    price = models.IntegerField(default=20.0)
    inventory_count = models.IntegerField(default=0)

    def to_json(self):
        return {
            "title": self.title,
            "price": self.price,
            "inventory_count": self.inventory_count
        }
