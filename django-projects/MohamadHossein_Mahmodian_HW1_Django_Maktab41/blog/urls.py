from django.urls import path
from .views import Category_single, Index, Single_post, Login_form, Logout_form, Register_view

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('<slug:slug>', Single_post, name="post_single"),
    path('categories/<slug:slug>', Category_single.as_view(), name='category_single'),
    path('login/', Login_form, name='login'),
    path('logout/', Logout_form, name='logout'),
    path('register/', Register_view, name='register'),
]
#