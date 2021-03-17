from django.urls import path
from .views import Index,product_single

app_name = 'siteview'

urlpatterns = [
    path('', Index, name="index"),
    path('product', product_single, name="product_single"),
]