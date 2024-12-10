from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='buyer')

    def __str__(self):
        return self.username

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    store_name = models.CharField(max_length=100)
    # Add any other fields you want the seller to have

    def __str__(self):
        return self.store_name
