from django.db import models
from products.models import Product

# Create your models here.
# class Customer(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.first_name}: {self.last_name}"


class Review(models.Model):
    rating = models.PositiveIntegerField()
    headline = models.CharField(max_length=100)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #user = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title}: {self.headline}"