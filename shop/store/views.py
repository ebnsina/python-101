import json
import stripe
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.core.paginator import Paginator
from .models import Product, Category, Order, OrderItem, Shipping

from .forms import ShippingForm

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    categories = Category.objects.all()
    
    try:
        customer = request.user.customer
    except:
        pass
    # order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    # items_count = order.get_cart_item
    # context =  { 'products': products, 'categories': categories, 'items_count': items_count }


    queryset = Product.objects.all()
    paginator = Paginator(queryset, 6)
    products = paginator.get_page(request.GET.get('page'))

    if request.method == 'POST':
        query = request.POST.get('query')
        # results = Product.objects.filter(title__icontains=query)
        results = Product.objects.filter(Q(title__icontains=query) | Q(price__icontains=query) )
        context =  { 'results': results, 'query': query}
        return render(request, 'store/search-result.html', context)


    context =  { 'products': products, 'categories': categories }
    return render(request, 'store/index.html', context)


def show(request):
    pass


def product_by_category(request, slug):
    products = Product.objects.filter(category__slug=slug)
    context =  { 'products': products }
    return render(request, 'store/index.html', context)


def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    items = order.orderitem_set.all() 
    items_count = order.get_cart_item
    context = {'items': items, 'items_count': items_count, 'order': order }
    return render(request, 'store/cart.html', context)


def checkout(request):
    form = ShippingForm()
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    items = order.orderitem_set.all() 
    items_count = order.get_cart_item
    context = {'items': items, 'items_count': items_count, 'order': order, 'form': form  }
    return render(request, 'store/checkout.html', context)


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


def place_order(request):
    data = json.loads(request.body)
    city = data['city']
    postcode = data['postcode']
    address = data['address']
    total = data['total']

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer)

    if order.get_cart_total == float(total):
        order.is_complete = True
    order.save()

    Shipping.objects.create(city=city, postcode=postcode, address=address, order=order, customer=customer)

    """ payment """
    session = stripe.checkout.Session.create(
    success_url=request.build_absolute_uri(reverse('thank_you')),
    cancel_url=request.build_absolute_uri(reverse('index')),
    line_items=[
        {
        "name": "Django Shop",
        "amount": str(int(order.get_cart_total) * 100),
        "quantity": order.get_cart_item,
        'currency': 'usd'
        },
        ],
    mode="payment",
    )

    # print(session)

    return JsonResponse({
        "message": "Order placed successfully.",
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'session_id': session.id
        }, safe=False)




def thank_you(request):
    return render(request, 'store/thank-you.html')








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