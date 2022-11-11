from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # test url
    path('', views.test, name='test'),
    path('signup/agreement/', views.agreement, name='agreement'),
    path('signup/<int:is_seller>/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('wishlist/', views.wishlist,name='wishlist')
]
