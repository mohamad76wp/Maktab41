from django.urls import path
from .views import index, single,category_single

urlpatterns = [
    path('', index, name="index"),
    path('<slug:slug>', single, name="post_single"),
    path('categories/<slug:slug>/', category_single, name='category_single'),
]
