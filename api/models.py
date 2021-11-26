from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True)
    price = models.FloatField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
