from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from products.models import Product
from reviews.models import Review
from django.contrib import messages


def test(request):
    context = {
        "products": Product.objects.all(),
    }

    return render(request, "accounts/test.html", context)


def agreement(request):
    if request.POST.get("agreement1", False) and request.POST.get("agreement2", False):
        request.session["agreement"] = True
        if request.POST.get("seller") == "seller":
            is_seller = 1
            return redirect("accounts:signup", is_seller)
        else:
            is_seller = 0
            return redirect("accounts:signup", is_seller)
    else:
        messages.info(request, "약관에 모두 동의해주세요.")
        return render(request, "accounts/agreement.html")
    # context = {
    #     'buyer': 0,
    #     'seller': 1,
    # }

    # return render(request, 'accounts/agreement.html', context)


def signup(request, is_seller):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save(commit=False).is_seller = is_seller
            form.save()

            # must change this statement
            return redirect("accounts:test")

    else:
        form = CustomUserCreationForm()

        # Hide address part of the form
        if is_seller:
            form.fields["address"].widget = forms.HiddenInput()

    context = {"form": form}

    return render(request, "accounts/form.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            # must change this statement
            return redirect(request.GET.get("next") or "accounts:test")

    else:
        form = AuthenticationForm(request)

    context = {"form": form}

    return render(request, "accounts/form.html", context)


def logout(request):
    auth_logout(request)

    # must change this statement
    return redirect("accounts:login")


def mypage(request):
    if request.user.is_seller:
        # 상품문의, 새로 작성된 리뷰, 팔로워 수
        # 데이터가 필요하다.
        pass
    else:
        # 적립금, 쿠폰, 팔로잉 수
        # 데이터가 필요하다.
        pass

    return render(request, "accounts/mypage.html")


def cart(request):
    products = request.user.carts.all()

    context = {
        "products": products,
    }

    return render(request, "accounts/cart.html", context)


def add_cart(request, product_id):
    cart = request.user.carts
    product = Product.objects.get(id=product_id)

    if product in cart.all():
        cart.remove(product)
    else:
        cart.add(product)

    # must change this statement
    return redirect("accounts:test")


def wishlist(request):
    context = {"wishlist": request.user.wishlist}

    return render(request, "accounts/wishlist.html", context)


def review(request):
    if request.user.is_seller:
        # 자신의 판매 상품 리뷰 목록을 보여준다.
        products = Product.objects.filter(user=request.user)
        reviews = []
        for product in products:
            reviews += product.review_set.all()
    else:
        # 자신이 작성한 리뷰 목록을 보여준다.
        reviews = Review.objects.filter(user=request.user)

    context = {"reviews": reviews}

    return render(request, "accounts/review.html", context)
