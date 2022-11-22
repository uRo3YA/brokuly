from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('go_order/<int:pk>', views.go_order, name='go_order'),
    path('create/', views.orders_create, name='create_order'), 
    path('complete/<int:pk>', views.orders_complete, name='create_complete'),
    path('detail/<int:pk>', views.orders_detail, name='detail_order'),
    path('pay/<int:pk>/', views.pay, name='pay'),
    path('success/<int:pk>/', views.success, name='success'),
    path('fail/<int:pk>/', views.fail, name='fail'),
    path('cancel/<int:pk>/', views.cancel, name='cancel'),
]