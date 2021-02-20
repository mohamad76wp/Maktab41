from django.urls import path
from .views import Category_single, Index, Single_post, Login_form, Logout_form, Register_view , Like_comment#,Create_comment
from .api import post_list , post_detail
urlpatterns = [
    path('', Index, name="index"),
    path('<slug:slug>', Single_post, name="post_single"),
    path('categories/<slug:slug>', Category_single, name='category_single'),
    path('login/', Login_form, name='login'),
    path('logout/', Logout_form, name='logout'),
    path('register/', Register_view, name='register'),
    path('json/posts/', post_list, name='post_list'),
    path('json/posts/<int:pk>', post_detail, name='post_detail'),
    path('like_comment/',Like_comment, name='like_comment'),
    # path('comment/',Create_comment,name='create_comment'),
]
