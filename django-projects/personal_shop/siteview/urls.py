from django.urls import path
from .views import Index

app_name = 'siteview'

urlpatterns = [
    path('', Index, name="index"),
]