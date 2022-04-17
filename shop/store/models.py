import uuid
from django.db import models

from account.models import Customer

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'



class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_complete = models.BooleanField(default=False)
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        return sum([item.get_total for item in orderitems])

    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        return sum([item.quantity for item in orderitems])

    


class OrderItem(models.Model):
    quantity = models.IntegerField(default=0)
    placed_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        return self.product.discount_price * self.quantity


class Shipping(models.Model):
    city = models.CharField(max_length=100)
    address = models.TextField()
    postcode = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.address
