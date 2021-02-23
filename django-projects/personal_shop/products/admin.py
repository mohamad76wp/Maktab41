from django.contrib import admin
from .models import Product, ShopProduct, Brand, Category, Discount, Comment, Like, Shop,         ProductMeta
# Register your models here.


class CommentTabAdmin(admin.TabularInline):
    model = Comment
    extra = 1


class LikeTabAdmin(admin.TabularInline):
    model = Like
    extra = 1


class DiscountTabAdmin(admin.TabularInline):
    model = Discount
    extra = 1


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "slug", "description", "logo")
    search_fields = ("name", "slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category", "slug", "image", "details")
    search_fields = ("name", "slug")
    list_filter = ("brand", "category")

    inlines = [
        CommentTabAdmin,
        LikeTabAdmin,
        DiscountTabAdmin,
    ]


@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ("shop", "product", "price", "quantity")
    search_fields = ("shop", "product")
    list_filter = ("shop", "product")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "details", "image")
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "details",)
    search_fields = ("name",)
    list_filter = ("category",)
