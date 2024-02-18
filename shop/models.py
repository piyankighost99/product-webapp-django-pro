from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    brand = models.CharField(max_length=10)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id})"