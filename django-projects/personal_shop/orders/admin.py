from django.contrib import admin
from .models import Order, OrderItem, Basket, BasketItem, Payment
# Register your models here.


class BasketItemTabAdmin(admin.TabularInline):
    model = BasketItem
    extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)
    list_per_page = 20

    inlines = [
        BasketItemTabAdmin,
    ]


class OrderItemTabAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'description')
    search_fields = ('user',)
    list_per_page = 20

    inlines = [
        OrderItemTabAdmin,
    ]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order","user","amount","status")
    list_per_page = 20
