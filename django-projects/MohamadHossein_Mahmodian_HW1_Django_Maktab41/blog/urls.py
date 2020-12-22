from django.urls import path
from .views import category_single, Index, single, login_form, logout_form, register_view

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('<slug:slug>', single, name="post_single"),
    path('categories/<slug:slug>', category_single, name='category_single'),
    path('login/', login_form, name='login'),
    path('logout/', logout_form, name='logout'),
    path('register/', register_view, name='register'),
]
