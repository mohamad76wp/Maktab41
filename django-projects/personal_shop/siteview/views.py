from django.shortcuts import render

# Create your views here.


def Index(request):
    context = {'1':'2'}
    
    return render(request, "site_view/index.html", context)

