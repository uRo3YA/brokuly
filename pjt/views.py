from django.shortcuts import render

from products.models import Product
from reviews.models import Review, ReviewImage
from django.db.models import Q, Count


def root(request):
    hot_items = Product.objects.all().order_by("-price")[0:4]
    sale_items = Product.objects.all().order_by("price")[0:4]
    hot_reviews = Product.objects.annotate(review_count=Count("review")).order_by(
        "-review_count"
    )[0:4]
    recent_review = ReviewImage.objects.annotate(
        review_count=Count("review_id")
    ).order_by("-id")[0:4]

    # for review_image in recent_review:

    context = {
        "hot_items": hot_items,
        "sale_items": sale_items,
        "hot_reviews": hot_reviews,
        "recent_review": recent_review,
    }

    return render(request, "main.html", context)
