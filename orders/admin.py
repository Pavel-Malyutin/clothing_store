from django.contrib import admin
from .models import Payment, Order, OrderProduct


class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'email', 'created_at', 'status', 'is_ordered']
    list_filter = ['status', 'is_ordered']
    list_per_page = 20
    inlines = [OrderProductInLine]


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(OrderProduct)
