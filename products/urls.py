from django.urls import path
from . import views
from qnas import views as qnas_views

#
app_name = "products"
urlpatterns = [
    path("<str:type>", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    # path("search", views.search, name="search"),
    path("search/", views.SearchView.as_view(), name="search"),
    #############################################
    # path("cart/", views.cart, name="cart")
    # path("add_cart/<int:pk>", views.add_cart, name="add_cart"),
    # path('<int:pk>/wishlist/', views.wishlist),
    #############################################
    path(
        "<int:pk>/qnas/question/create/",
        qnas_views.question_create,
        name="question_create",
    ),
]
