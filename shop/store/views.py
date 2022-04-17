import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Product, Category, Order, OrderItem

def index(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-created_at')
    context =  { 'products': products, 'categories': categories }
    return render(request, 'store/index.html', context)


def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    items = order.orderitem_set.all() 
    items_count = order.get_cart_item
    context = {'items': items, 'items_count': items_count, 'order': order }
    return render(request, 'store/cart.html', context)



def checkout(request):
    pass


def add_to_cart(request):
    data = json.loads(request.body)
    id = data['id']
    action = data['action']

    customer = request.user.customer
    product = get_object_or_404(Product, id=id)
    order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'increment':
        orderItem.quantity += 1
    elif action == 'decrement':
        orderItem.quantity -= 1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse({ 'message': 'Add To Cart successfully'}, safe=False)






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