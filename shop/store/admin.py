from django.contrib import admin

from .models import Category, Product, Order, OrderItem, Shipping

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('title', 'slug','created_at')
   prepopulated_fields = {'slug': ('title', ) }


class ProductAdmin(admin.ModelAdmin):
   list_display = ('title', 'slug', 'image', 'price', 'discount_price', 'created_at', 'category')
   search_fields = ['slug']
   prepopulated_fields = {'slug': ('title', ) }


class OrderAdmin(admin.ModelAdmin):
    pass

class OrderItemAdmin(admin.ModelAdmin):
    pass

class ShippingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Shipping, ShippingAdmin)
