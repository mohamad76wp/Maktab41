from django.shortcuts import render
from .models import Carousel,Carousel_image 
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()


def Index(request):
    carousel = Carousel_image.objects.filter(carousel_id=3)
    context = {'carousel':carousel}
    
    return render(request, "site_view/index.html", context)

