from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.orders_create, name='create_order'),
    path('complete/<int:pk>', views.orders_complete, name='create_complete'),
    path('detail/<int:pk>', views.orders_detail, name='detail_order'),
]