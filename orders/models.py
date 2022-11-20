from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product, related_name='products_order')
    products = models.TextField(null=True,blank=True)
    # carts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='carts_order')
    total_quantity = models.IntegerField(default=False)
    shipping_price = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mileage = models.IntegerField()
    status = models.IntegerField(default=0)