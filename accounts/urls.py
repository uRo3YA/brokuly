from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/agreement/', views.agreement, name='agreement'),
    path('signup/<int:is_seller>/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
