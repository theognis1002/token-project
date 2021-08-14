from django.db import models
from products.managers import SoftDeleteManager


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    qty = models.IntegerField(default=1)
    price = models.FloatField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    soft_delete = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return self.name
