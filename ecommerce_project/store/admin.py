from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Review


# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Product, ProductAdmin)

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product']}),
        ('Quantity', {'fields': ['quantity']}),
        ('Price', {'fields': ['price']}),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    max_num = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_link = ['id', 'billingName']
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created', 'billingName', 'billingAddress'
                       ,'shippingName', 'shippingAddress']
    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
        ('BILLING INFORMATION', {'fields': ['billingName', 'billingAddress']}),
        ('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddress']}),
    ]

    inlines = [OrderItemAdmin,
               ]

    def has_detele_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Review)


