from django.urls import path
from .views import index, single

urlpatterns = [
    path('', index,name = "index"),
    path('<slug:slug>',single,name = "post_single")
]