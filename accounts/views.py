from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate,
    update_session_auth_hash,
    get_user_model,
)
from products.models import Product
from reviews.models import Review, ReviewImage
from django.http import JsonResponse
import json
from .models import User
from qnas.models import Question
from django.core.paginator import Paginator
from qnas.models import Question, Answer
from qnas.forms import QuestionForm, AnswerForm
from django.contrib.auth.hashers import check_password

from accounts.decorators import seller_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from collections import defaultdict

from random import random
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from orders.models import Order

# 회원가입 약관
def agreement(request):
    if request.method == "POST":
        data = request.POST.get("buyer") or request.POST.get("seller")

        if data == "buyer":
            is_seller = 0
        else:
            is_seller = 1

        return redirect("accounts:signup", is_seller)

    else:
        return render(request, "accounts/agreement.html")


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

    return render(request, "accounts/signup.html", context)


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

        # update placeholder in login form(AuthenticationForm)
        form.fields['username'].widget.attrs.update({'placeholder': '아이디를 입력해주세요.'})
        form.fields['password'].widget.attrs.update({'placeholder': '비밀번호를 입력해주세요.'})

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)


# 로그아웃
@login_required
def logout(request):
    auth_logout(request)

    # must change this statement
    return redirect("accounts:login")


# 마이페이지
@login_required
def mypage(request):
    reviews = Review.objects.filter(user=request.user)

    if request.user.is_seller:
        # 상품문의, 새로 작성된 리뷰, 팔로워 수
        # 데이터가 필요하다.
        products = Product.objects.filter(user=request.user)
        questions = Question.objects.filter(product__in=products)

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

    return render(request, "accounts/mypage.html", context)


# 장바구니
@login_required
def cart(request):
    products = request.user.carts.all()

    context = {
        "products": products,
    }

    return render(request, "accounts/cart.html", context)


# 장바구니 상품 추가
@login_required
def add_cart(request, product_id):
    cart = request.user.carts
    product = Product.objects.get(id=product_id)

    if product in cart.all():
        cart.remove(product)
        in_cart = False
    else:
        cart.add(product)
        in_cart = True

    context = {
        "in_cart": in_cart,
        "cart_length": cart.count(),
    }

    return JsonResponse(context)


# 장바구니 상품 추가 후 장바구니로 리다이렉트
@login_required
def add_cart_redirect(request, product_id):
    cart = request.user.carts
    product = Product.objects.get(id=product_id)

    if product in cart.all():
        cart.remove(product)
    else:
        cart.add(product)

    return redirect("accounts:cart")


# 위시리스트 목록
@login_required
def wishlist(request):
    context = {
        "wishlist": request.user.wishlist.all(),
        "cart": request.user.carts.all(),
    }

    return render(request, "accounts/mypage_wishlist.html", context)


# 위시리스트 상품 추가
@login_required
def add_wishlist(request, product_id):
    user_wishlist = request.user.wishlist
    product = Product.objects.get(id=product_id)

    if product in user_wishlist.all():
        user_wishlist.remove(product)
        is_liked = False
    else:
        user_wishlist.add(product)
        is_liked = True

    context = {"isLiked": is_liked}

    return JsonResponse(context)


# 리뷰 목록
@login_required
def review(request):
    ###페이지 상단에 문의 갯수 표시용
    questions = ""
    if request.user.is_seller:
        # 자신의 판매 상품 리뷰 목록을 보여준다.
        products = Product.objects.filter(user=request.user)
        ###페이지 상단에 문의 갯수 표시용
        questions = Question.objects.filter(product_id__in=products)
        review_image = ReviewImage.objects.all()
        reviews = []
        for product in products:
            reviews += product.review_set.all()
    else:
        # 자신이 작성한 리뷰 목록을 보여준다.
        reviews = Review.objects.filter(user=request.user)
        review_image = ReviewImage.objects.all()
        # reviews_image = Review.objects.prefetch_related("reviewimage_set").filter(
        #     review_id__in=reviews
        # )
    context = {"reviews": reviews, "questions": questions, "review_image": review_image}

    return render(request, "accounts/mypage_review.html", context)


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
    user_id = jsonObject.get("user_id")

    if User.objects.filter(username=user_id):
        is_exist = True
    else:
        is_exist = False

    context = {"is_exist": is_exist}
    return JsonResponse(context)


# 이메일 중복체크
def check_email(request):
    jsonObject = json.loads(request.body)
    user_email = jsonObject.get("user_email")

    if User.objects.filter(email=user_email):
        is_exist = True
    else:
        is_exist = False

    context = {"is_exist": is_exist}
    return JsonResponse(context)


def id_check(request):
    jsonObject = json.loads(request.body)
    username = jsonObject.get("username")
    username = "k" + str(username)
    print(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        email = jsonObject.get("email")
        name = jsonObject.get("nickname")
        user = User.objects.create(username=username, email=email, name=name)
        user.save()
    auth_login(request, user, backend="django.contrib.auth.backends.ModelBackend")
    return JsonResponse(
        {
            "username": user.username,
            "email": user.email,
            "name": user.name,
        }
    )


def id_check_naver(request):
    jsonObject = json.loads(request.body)
    username = jsonObject.get("id")
    username = "n" + str(username)
    print(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        email = jsonObject.get("email")
        name = jsonObject.get("name")
        user = User.objects.create(username=username, email=email, name=name)
        user.save()
    auth_login(request, user, backend="django.contrib.auth.backends.ModelBackend")
    return JsonResponse(
        {
            "username": user.username,
            "email": user.email,
            "name": user.name,
        }
    )


def naver_callback(request):
    return render(request, "accounts/naver_callback.html")


### 상품정보 관리
@seller_required
def product_management(request):
    if request.user.is_seller:
        # 자신의 판매 상품 목록을 보여준다.
        products = Product.objects.filter(user=request.user)
        questions = Question.objects.filter(product_id__in=products)
        # 입력 파라미터
        page = request.GET.get("page", "1")
        # 페이징
        paginator_all = Paginator(products, 5)
        products = paginator_all.get_page(page)
    else:
        return redirect("accounts:mypage")

    context = {
        "products": products,
        "questions": questions,
    }

    return render(request, "accounts/mypage_product_management.html", context)


###주문자가 판매자에게 한 문의 모아보기
@seller_required
def question_management(request, type):
    # so = request.GET.get("so", "recent")  # 정렬기준
    # 정렬
    # print(so)
    answer_form = AnswerForm()
    reviews = Review.objects.filter(user=request.user)
    if request.user.is_seller:
        # 자신의 판매 상품 목록을 보여준다.
        products = Product.objects.filter(user=request.user)
        so = type
        if so == "unanswer":
            questions = Question.objects.filter(
                product_id__in=products
            ) & Question.objects.filter(is_answered=0)
        elif so == "answered":

            questions = Question.objects.filter(
                product_id__in=products
            ) & Question.objects.filter(is_answered=1)
        else:  # recent
            questions = Question.objects.filter(product_id__in=products)

        # 입력 파라미터
        page = request.GET.get("page", "1")
        # 페이징
        paginator_all = Paginator(products, 5)
        products = paginator_all.get_page(page)
    else:
        return redirect("accounts:mypage")

    context = {
        "products": products,
        "questions": questions,
        "answer_form": answer_form,
        "reviews": reviews,
    }

    return render(request, "accounts/mypage_question_management.html", context)


### 주문자 자신의 문의 모아 보기
@login_required
def myquestion(request):
    questions = Question.objects.filter(user=request.user)
    answers = Answer.objects.all()
    reviews = Review.objects.filter(user=request.user)
    print(len(reviews))
    context = {"questions": questions, "answers": answers, "reviews": reviews}
    return render(request, "accounts/mypage_question.html", context)


# 회원정보 수정
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            # 비밀번호가 변경되면 기존 세션과 회원 인증 정보가
            # 일치하지 않게 되기 때문에 새로운 password hash 로
            # 세션을 업데이트 해주는 메소드이다.
            update_session_auth_hash(request, form.user)

            return redirect("accounts:mypage")

    else:
        form = CustomUserChangeForm(request.user)

    context = {
        "form": form,
    }

    return render(request, "accounts/update_profile.html", context)


# 회원 탈퇴
def signout(request):
    if request.method == "POST":
        password = request.POST.get("checkPassword")

        user = check_password(password, request.user.password)

        if user:
            request.user.delete()

            return redirect("root")
        else:
            return redirect("accounts:signout")
    else:
        return render(request, "accounts/signout.html")


### 상품 페이지에서 팔로잉(비동기)
def follow(request, product_user_id):
    # 프로필에 해당하는 유저를 로그인한 유저가!
    # person = User.objects.get(pk=request.user.id)

    user_followings = request.user.followings
    product_user = User.objects.get(id=product_user_id)

    if product_user in user_followings.all():
        user_followings.remove(product_user)
        isFollowed = False
    else:
        user_followings.add(product_user)
        isFollowed = True

    context = {"isFollowed": isFollowed}

    return JsonResponse(context)


def followlist(request):
    following = get_user_model().objects.filter(following_user=request.user.pk)
    print(following)
    products = Product.objects.filter(user_id__in=following).order_by("-id")
    product_list = defaultdict(list)
    product_ = []
    for seller in following:
        for product in products:
            if seller.id == product.user_id:
                product_list[seller.id].append(product.id)
    for key, val in product_list.items():
        product_.append({"key": key, "val": val[:4]})

    print(product_)
    context = {
        "products": products,
        "following": following,
        "product_list": product_list,
        "product_": product_,
    }
    return render(request, "accounts/mypage_following.html", context)


### 마이페이지에서 언팔로잉
def unfollow(request, product_user_id):
    user_followings = request.user.followings
    product_user = User.objects.get(id=product_user_id)

    if product_user in user_followings.all():
        user_followings.remove(product_user)
        isFollowed = False
    else:
        user_followings.add(product_user)
        isFollowed = True

    return redirect("accounts:followlist")


def send_valid_number(request):
    validnumber = round(random() * 10000)

    current_site = get_current_site(request)
    message = render_to_string(
        "accounts/working/send_validnumber.html",
        {
            "user": request.user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(request.user.pk))
            .encode()
            .decode(),
            "validnumber": validnumber,
        },
    )
    mail_subject = "[Brokurly]이메일 인증번호입니다."
    user_email = json.loads(request.body)["user_email"]
    email = EmailMessage(mail_subject, message, to=[user_email])
    email.send()

    context = {
        "validnumber": validnumber,
    }
    return JsonResponse(context)


def check_valid_number(request):
    valid_number = json.loads(request.body)["valid_number"]
    input_number = json.loads(request.body)["input_number"]
    print(valid_number, input_number)
    if valid_number == input_number:
        check = True
    else:
        check = False
    context = {
        "check": check,
    }
    return JsonResponse(context)


def orderlist(request):
    # Order.objects.get(pk=1).delete()
    # Order.objects.get(pk=2).delete()
    orders = Order.objects.filter(user=request.user) & Order.objects.exclude(status=0)
    jsonDec = json.decoder.JSONDecoder()

    for order in orders:
        order.products = Product.objects.get(
            pk=jsonDec.decode(order.products)[0]["product_pk"]
        )
        print(order.products)
    context = {
        "orders": orders,
    }
    return render(request, "accounts/orderlist_buyer_mypage.html", context)
