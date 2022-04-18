from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('thank_you/', views.thank_you, name='thank_you'),

    # ajax
    path('test/', views.test, name='test'),
    path('posts/', views.posts, name='posts'),
]
