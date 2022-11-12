from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from .models import Cart
from reviews.models import Review
from accounts.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from collections import Counter

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
    # cart = AddProductForm(initial={"quantity": 1})
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


# def cart(request):
#     cart_item = Cart.objects.filter(user__id=request.user.pk)
#     # 장바구니에 담긴 상품의 총 합계 가격
#     total_price = 0
#     total_quantity = 0
#     dic = {}
#     for cart in cart_item:
#         if cart.products.pk in dic:
#             dic[cart.products.pk] += cart.quantity
#         else:
#             dic[cart.products.pk] = 1
#     print(dic)
#     # for loop 를 순회하여 각 상품 * 수량을 total_price 에 담는다
#     for each_total in cart_item:
#         total_price += each_total.products.price * each_total.quantity
#         total_quantity += each_total.quantity
#     if cart_item is not None:
#         context = {
#             # 없으면 없는대로 빈 conext 를 템플릿 변수에서 사용
#             "cart_item": cart_item,
#             "total_price": total_price,
#             "total_quantity": total_quantity,
#             "dic":dic
#         }

#         return render(request, "products/cart.html", context)
#     return redirect("/")


def add_cart(request, pk):
    if request.method == "POST":
        selected_product = Product.objects.get(pk=pk)
        selected_quantity = int(request.POST.get("p_num1"))
        # stock_now = Product.objects.get(id=selected_inventory).stock
        print("selected_inventory:", selected_product)
        print("selected_quantity:", selected_quantity)
        cart = Cart()
        cart.user = request.user
        cart.products = selected_product
        cart.quantity = selected_quantity
        cart.save()
        # request.pk -> 개인 장바구니 페이지 연결 필요
        return redirect("/")
