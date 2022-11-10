from django.db import models
from .choice import ALLERGY_CHOICES
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, Thumbnail
import os
from django.conf import settings
from multiselectfield import MultiSelectField

#
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    unit = models.CharField(max_length=64)
    weight = models.CharField(max_length=64)
    produt_thum_img = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(500, 350)],
        format="JPEG",
        options={"quality": 80},
    )
    produt_detail_img = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(500, 350)],
        format="JPEG",
        options={"quality": 80},
    )
    produt_desc_img = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(500, 350)],
        format="JPEG",
        options={"quality": 80},
    )
    description = description = models.TextField(blank=True)
    stock = models.IntegerField()
    sales_rate = models.PositiveIntegerField()

    allergy = MultiSelectField(
        choices=ALLERGY_CHOICES,
    )
    # wishlist=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wishlist_product')
    def delete(self, *args, **kargs):
        if self.produt_thum_img:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.produt_thum_img.path))
        if self.produt_desc_img:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.produt_desc_img.path))
        super(Product, self).delete(*args, **kargs)

    class Meta:
        db_table = "상품"
        verbose_name = "상품"
        verbose_name_plural = "상품"
