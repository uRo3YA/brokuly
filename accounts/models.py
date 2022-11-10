from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None

    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150, blank=True)
    is_seller = models.BooleanField(default=False)

    wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'wishlist_user')
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'following_user')
    carts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'carts_user')