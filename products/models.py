from django.db import models
from users.models import User

class Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'seller'})
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

# products/models.py
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')  # Tied to the seller/shop

    def __str__(self):
        return self.name

