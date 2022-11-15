from django.shortcuts import render

from products.models import Product
from django.db.models import Q, Count


def root(request):
    hot_items = Product.objects.all().order_by("-price")[0:4]
    sale_items = Product.objects.all().order_by("price")[0:4]
    hot_reviews = Product.objects.annotate(review_count=Count("review")).order_by(
        "-review_count"
    )[0:4]

    context = {
        "hot_items": hot_items,
        "sale_items": sale_items,
        "hot_reviews": hot_reviews,
    }

    return render(request, "main.html", context)
