from django.urls import path
from . import views

#
app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("add_cart/<int:pk>", views.add_cart, name="add_cart")
    # path('search', views.search, name='search'),
    # path('<int:pk>/wishlist/', views.wishlist),
]
