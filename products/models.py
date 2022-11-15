from django.db import models
from .choice import ALLERGY_CHOICES
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, Thumbnail
import os
from django.conf import settings
from multiselectfield import MultiSelectField

ship_Choices = (
    ("샛별배송", "샛별배송"),
    ("일반택배", "일반택배"),
)
#
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    ship_type = models.CharField(max_length=10, choices=ship_Choices)
    allergy = MultiSelectField(
        choices=ALLERGY_CHOICES,
    )
    is_crawl = models.BooleanField(default=False)
    crawl_produt_thum_img = models.TextField(blank=True)
    crawl_produt_detail_img = models.TextField(blank=True)
    crawl_produt_desc_img = models.TextField(blank=True)
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


# 일단 장바구니 구현 ->> 이동 필요, accunts앱으로?
class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    products = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="wish_product", blank=True
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "{} // {}".format(self.user, self.products.name)

    def sub_total(self):
        # 템플릿에서 사용하는 변수로 장바구니에 담긴 각 상품의 합계
        return self.products.price * self.quantity
