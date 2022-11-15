from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from products.models import Product
from reviews.models import Review
from django.http import JsonResponse
import json
from .models import User
from qnas.models import Question

# 회원가입 약관
def agreement(request):
    if request.method == 'POST':
        data = request.POST.get('buyer') or request.POST.get('seller')

        if data == 'buyer':
            is_seller = 0
        else:
            is_seller = 1

        return redirect("accounts:signup", is_seller)

    else:
        return render(request, "accounts/complete/agreement.html")


# 회원가입
def signup(request, is_seller):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save(commit=False).is_seller = is_seller
            form.save()

            return redirect("accounts:login")

    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
        "is_seller": is_seller,     
    }

    return render(request, "accounts/complete/signup.html", context)


# 로그인
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            # must change this statement
            return redirect(request.GET.get("next") or "root")

    else:
        form = AuthenticationForm(request)

    context = {
        "form": form,
    }

    return render(request, "accounts/complete/login.html", context)


# 로그아웃
def logout(request):
    auth_logout(request)

    # must change this statement
    return redirect("accounts:login")


# 마이페이지
def mypage(request):
    reviews = Review.objects.filter(user=request.user)

    if request.user.is_seller:
        # 상품문의, 새로 작성된 리뷰, 팔로워 수
        # 데이터가 필요하다.
        products = Product.objects.filter(user=request.user)
        questions = []
        
        for product in products:
            questions += product.question_set.all()

        context = {
            "products": products,
            "reviews": reviews,
            "questions": questions,
        }

    else:
        # 적립금, 쿠폰, 팔로잉 수
        # 주문 내역, 위시리스트 목록, 상품 후기 목록, 상품 문의 목록
        # 데이터가 필요하다.
        questions = Question.objects.filter(user=request.user)

        context = {
            "reviews": reviews,
            "questions": questions,
        }

    return render(request, "accounts/working/mypage.html", context)


# 장바구니
def cart(request):
    products = request.user.carts.all()

    context = {
        "products": products,
    }

    return render(request, "accounts/cart.html", context)


# 장바구니 추가
def add_cart(request, product_id):
    cart = request.user.carts
    product = Product.objects.get(id=product_id)

    if product in cart.all():
        cart.remove(product)
    else:
        cart.add(product)

    # must change this statement
    return redirect("accounts:test")


# 위시리스트 목록
def wishlist(request):
    context = {"wishlist": request.user.wishlist}

    return render(request, "accounts/wishlist.html", context)


# 리뷰 목록
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

    context = {
        "reviews": reviews,
    }

    return render(request, "accounts/working/mypage_review.html", context)


# 개인정보 수정 확인(미완성)
def check(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.data["username"], password=form.data["password"]
            )
            check = request.user.username == user.get_username()

            if check:
                return redirect("accounts:update")
            else:
                return redirect("accounts:check")

    else:
        form = AuthenticationForm(request)

    context = {"form": form}

    return render(request, "accounts/form.html", context)

# 아이디 중복체크
def check_id(request):
    jsonObject = json.loads(request.body)
    user_id= jsonObject.get('user_id')

    if User.objects.filter(username=user_id):
        is_exist = True
    else:
        is_exist = False

    context = {'is_exist': is_exist}
    return JsonResponse(context) 

def id_check(request):
    jsonObject = json.loads(request.body)
    username = jsonObject.get('username')
    username = "k" + str(username)
    print(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        email = jsonObject.get('email')
        name = jsonObject.get('nickname')
        user = User.objects.create(username=username, email=email, name=name)
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return JsonResponse({'username': user.username, 'email': user.email, 'name':user.name,})

def id_check_naver(request):
    jsonObject = json.loads(request.body)
    username = jsonObject.get('id')
    username = "n" + str(username)
    print(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        email = jsonObject.get('email')
        name = jsonObject.get('name')
        user = User.objects.create(username=username, email=email, name=name)
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return JsonResponse({'username': user.username, 'email': user.email, 'name':user.name,})

def naver_callback(request):
    return render(request, 'accounts/complete/naver_callback.html')