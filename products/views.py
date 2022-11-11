from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from reviews.models import Review

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

    context = {
        "Product_Form": Product_Form
    }

    return render(request, "products/form.html", context=context)


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    review = Review.objects.filter(product_id=product.pk)

    context = {
        "product": product,
        "reviews": review,
    }

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
