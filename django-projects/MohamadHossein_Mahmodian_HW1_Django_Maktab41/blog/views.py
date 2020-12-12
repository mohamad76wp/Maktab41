from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Category
from django.urls import reverse
from django.template import loader
# Create your views here.


def index(request):
    posts = Post.objects.all()

    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
    }

    return render(request, "blog/posts.html", context)


def single(request, slug):

    post = Post.objects.select_related('category',).get(slug=slug)
    categories = Category.objects.all()
        

    context = {
        'post': post,
        'category':post.category,
        'categories': categories,
        'comment': post.comment.filter(is_confirmed=True)
    }

    return render(request, "blog/post_single.html", context)


def category_single(request):
    pass