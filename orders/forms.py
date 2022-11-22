from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='products_order')
    # carts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='carts_order')
    total_quantity = models.IntegerField(default=False)
    shipping_price = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)