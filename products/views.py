from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, AddProductForm
from .models import Product
from reviews.models import Review
from accounts.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse

#
# Create your views here.
def index(request):
    contents = Product.objects.all()

    context = {
        "contents": contents,
    }

    return render(request, "products/index.html", context)


def create(request):
    if request.method == "POST":
        Product_Form = ProductForm(request.POST, request.FILES)

        if Product_Form.is_valid():
            product = Product_Form.save(commit=False)
            product.user = request.user
            product.save()

            return redirect("products:index")

    else:
        Product_Form = ProductForm()

    context = {"Product_Form": Product_Form}

    return render(request, "products/form.html", context=context)


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    review = Review.objects.filter(product_id=product.pk)
    cart = AddProductForm(initial={"quantity": 1})
    context = {"product": product, "reviews": review, "cart": cart}

    return render(request, "products/detail.html", context)


def update(request, pk):
    info = Product.objects.get(pk=pk)

    if request.method == "POST":
        Product_Form = ProductForm(request.POST, request.FILES, instance=info)

        if Product_Form.is_valid():
            info.save()
            Product_Form.save()

            return redirect("products:detail", info.pk)

    else:
        Product_Form = ProductForm(instance=info)

    context = {
        "Product_Form": Product_Form,
    }

    return render(request, "products/update.html", context)


def delete(request, pk):
    info = Product.objects.get(pk=pk)
    info.delete()

    return redirect("products:index")


def cart(request, pk):

    print(request.POST)
    review = get_object_or_404(Product, pk=pk)
    # comment_form = AddProductForm(request.POST)
    # if comment_form.is_valid():
    #     comment = comment_form.save(commit=False)
    #     comment.review = review
    #     # comment.user = request.user
    #     comment.save()
    #     context = {
    #         "content": comment.content,
    #         #'userName': comment.user.username
    #     }
    return redirect("products:cart")
