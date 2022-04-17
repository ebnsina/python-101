from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Category

def index(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-created_at')
    return render(request, 'store/index.html', {
        'products': products,
        'categories': categories,
    })


dummy_posts = [ 
    { 'id': 1, 'title': 'My first post', 'author': 'ebnsina', 'is_published': True },
    { 'id': 2, 'title': 'My 2nd post', 'author': 'ebnsina', 'is_published': True },
    { 'id': 3, 'title': 'My 3rd post', 'author': 'ebnsina', 'is_published': True },
    { 'id': 4, 'title': 'My 4th post', 'author': 'ebnsina', 'is_published': True },
    { 'id': 5, 'title': 'My 5th post', 'author': 'ebnsina', 'is_published': True },
    { 'id': 6, 'title': 'My 6th post', 'author': 'ebnsina', 'is_published': True },
]


def posts(request):
    return JsonResponse(dummy_posts, safe=False)


def test(request):
    return render(request, 'store/test.html')