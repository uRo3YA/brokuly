from django.urls import path
from . import views

app_name = 'qnas'

urlpatterns = [
    # path('products/<int:product_id>/', views.index, name='index'),
    # path('products/<int:product_id>/qnas/question/create/', views.question_create, name='question_create'),

    # path('qnas/question/create/', views.question_create, name='question_create'),
    path('<int:pk>/update/', views.question_update, name='question_update'),
    path('<int:pk>/delete/', views.question_delete, name='question_delete'),

    # path('products/<int:product_id>/', views.index, name='index'),
    # path('products/<int:product_id>/qnas/<int:question_id>/answer/create/', views.answer_create, name='answer_create'),

    path('<int:pk>/answer/create/', views.answer_create, name='answer_create'),
    path('answer/<int:pk>/update/', views.answer_update, name='answer_update'),
    path('answer/<int:pk>/delete/', views.answer_delete, name='answer_delete'),
]
