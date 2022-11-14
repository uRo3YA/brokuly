from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

from .forms import ReviewForm, CommentForm
from .models import Review, Comment, ReviewImage
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {"reviews": reviews}

    return render(request, "reviews/index.html", context)


def detail(request, pk):
    # review = get_object_or_404(Review, pk=pk)
    ##
    # prefetch_related를 통해 review를 상속받는 reveiwimage의 image들을 가져온다.
    # reveiwimage_set의 reveiwimage는 DB에 저장된 이름이다
    # review에 대한 query를 실행해 pk에 대한 리뷰를 받아오고,
    # 가져온 데이터에서 review의 id에 대해 reveiwimage의 query를 실행해 데이터를 가져온다
    review = Review.objects.prefetch_related("reviewimage_set").get(id=pk)
    comment_form = CommentForm()

    context = {
        "review": review,
        "comments": review.comment_set.all(),
        "comment_form": comment_form,
    }

    return render(request, "reviews/detail.html", context)


def review_create(request, pk):
    info = Product.objects.get(pk=pk)

    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            new = review_form.save(commit=False)
            new.product_id = info.pk
            new.user = request.user
            new.save()
            for image in request.FILES.getlist("image", None):
                postimage = ReviewImage()
                postimage.image = image
                postimage.review = new
                postimage.save()
            return redirect("products:detail", info.pk)

    else:
        review_form = ReviewForm()

    context = {"review_form": review_form}

    return render(request, "reviews/form.html", context=context)


def review_detail(request, product_pk, review_pk):
    info = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()

    context = {
        "info": info,
        "comment_form": comment_form,
        "comments": info.comment_set.all(),
    }

    return render(request, "reviews/detail.html", context)


def comment_create(request, pk):
    print(request.POST)
    review = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        # comment.user = request.user
        comment.save()
        context = {
            "content": comment.content,
            #'userName': comment.user.username
        }
        return JsonResponse(context)


def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    # if comment.user == request.user:
    #     comment.delete()
    return redirect("reviews:detail", pk)
