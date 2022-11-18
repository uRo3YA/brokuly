from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/agreement/", views.agreement, name="agreement"),
    path("signup/<int:is_seller>/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("mypage/", views.mypage, name="mypage"),
    path("cart/", views.cart, name="cart"),
    path("cart/add/<int:product_id>/", views.add_cart, name="add_cart"),
    path(
        "cart/add/<int:product_id>/redirect/",
        views.add_cart_redirect,
        name="add_cart_redirect",
    ),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wishlist/add/<int:product_id>/", views.add_wishlist, name="add_wishlist"),
    path("review/", views.review, name="review"),
    path("check/", views.check, name="check"),
    path("check_id/", views.check_id, name="check_id"),
    path("check/update/", views.update, name="update"),
    path("login/naver_callback/", views.naver_callback, name="naver_callback"),
    path("id_check/", views.id_check, name="id_check"),
    path("id_check_naver/", views.id_check_naver, name="id_check_naver"),
    ##
    path("product_management/", views.product_management, name="product_management"),
    ### 내 제품 문의사항 모아보기
    path("question_management/", views.question_management, name="question_management"),
    ### 내가 한 문의사항 모아보기myquestion
    path("myquestion/", views.myquestion, name="myquestion"),
    path("signout/", views.signout, name="signout"),
    ### 팔로잉 버튼
    path("follow/<int:product_user_id>/", views.follow, name="follow"),
    ###팔로잉 리스트
    path("followlist", views.followlist, name="followlist"),
    ### 언팔로잉 버튼
    path("unfollow/<int:product_user_id>/", views.unfollow, name="unfollow"),
    path("orderlist/", views.orderlist, name="orderlist"),
    path("send_valid_number/", views.send_valid_number, name="send_valid_number"),
    path("check_valid_number/", views.check_valid_number, name="check_valid_number"),
]
