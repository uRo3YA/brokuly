from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/create/", views.review_create, name="review_create"),
    path("<int:pk>/detail/<int:review_pk>", views.review_detail, name="review_detail"),
]
