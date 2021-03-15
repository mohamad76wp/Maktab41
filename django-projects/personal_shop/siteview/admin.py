from django.contrib import admin
from .models import Carousel,Carousel_image
# Register your models here.


class  ImageInline(admin.TabularInline):
    model = Carousel_image

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    search_fields = ("name",)
    inlines=[
        ImageInline
    ]