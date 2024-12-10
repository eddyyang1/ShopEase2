# products/models.py
from django.db import models
from users.models import Seller

class Shop(models.Model):
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='')  # Set a default value here
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name
