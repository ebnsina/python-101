from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),

    # ajax
    path('test/', views.test, name='test'),
    path('posts/', views.posts, name='posts'),
]
