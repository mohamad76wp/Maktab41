from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.urls import reverse
from django.template import loader
# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, "blog/posts.html", context)


def single(request, slug):

    post = Post.objects.get(slug=slug)

    context = {
        'posts': post,
    }

    return render(request, "blog/post_single.html", context)
