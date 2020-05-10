from django.db import models

# Create your models here.

class Product(models.Model):
    price = models.FloatField()
    title = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.title