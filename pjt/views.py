from django.shortcuts import render

from products.models import Product
from reviews.models import Review, ReviewImage
from django.db.models import Q, Count


def root(request):
    hot_items = Product.objects.all().order_by("-price")[0:4]
    hot_items_1 = Product.objects.all().order_by("-price")[4:8]
    sale_items = Product.objects.all().order_by("price")[0:4]
    sale_items_1 = Product.objects.all().order_by("price")[4:8]
    hot_reviews = Product.objects.annotate(review_count=Count("review")).order_by(
        "-review_count"
    )[0:4]
    hot_reviews_1 = Product.objects.annotate(review_count=Count("review")).order_by(
        "-review_count"
    )[4:8]
    recent_review = ReviewImage.objects.annotate(
        review_count=Count("review_id")
    ).order_by("-id")[0:5]
    md_pick = Product.objects.all().order_by("id")[0:4]
    md_pick_1 = Product.objects.all().order_by("id")[4:8]
    # recent_review = Review.objects.all().order_by("-id")[0:4]
    # recent_review_image = ReviewImage.objects.filter(review_id__in=recent_review)[0]
    # print(recent_review_image)
    # for i in range(4):
    #     print(recent_review[i].title)
    #     # print(recent_review_image[i].review_id)
    context = {
        "hot_items": hot_items,
        "hot_items_1": hot_items_1,
        "sale_items": sale_items,
        "sale_items_1": sale_items_1,
        "hot_reviews": hot_reviews,
        "hot_reviews_1": hot_reviews_1,
        "recent_review": recent_review,
        "md_pick": md_pick,
        "md_pick_1": md_pick_1,
    }

    return render(request, "main.html", context)
