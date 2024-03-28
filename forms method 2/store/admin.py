from django.contrib import admin
from .models import Product, Collection, Customer, Order
# Register your models here
admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin Interface'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description',
                    'price', 'inventory', 'inventory_status', 'collection']
    list_editable = ['price']
    list_select_related = ['collection']
    ordering = ['id']
    list_per_page = 5

    @admin.display(ordering='inventory')
    def inventory_status(self, p: Product):
        if p.inventory > 20:
            return 'High'
        else:
            return 'Low'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    ordering = ['id']
    # list_select_related = ['promotions']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'phone', 'membership', 'points']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'place_at',
                    'payment_status', 'full_name', 'customer_email']
    # list_editable=['payment_status']
    ordering = ['id']
    list_per_page = 10

    def customer_email(self, Order):
        return Order.customer.email

    def full_name(self, o: Order):
        return f'{o.customer.first_name} {o.customer.last_name}'
