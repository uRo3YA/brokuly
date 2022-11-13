from django.db import models
from django.conf import settings
from products.models import Product


# Create your models here.
class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    # created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=0)
    # is_secret = models.BooleanField(default=0)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    # created_at = models.DateTimeField(auto_now_add=True)