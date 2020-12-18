from django.urls import path
from .views import category_single , Index,Single

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('<slug:slug>', Single.as_view(), name="post_single"),
    path('categories/<slug:slug>', category_single, name='category_single'),
]
