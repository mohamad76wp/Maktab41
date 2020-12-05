from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.urls import reverse
from django.template import loader
# Create your views here.


def index(request):
    posts = Post.objects.all()

    template = loader.get_template('blog/posts.html')
    context = {
        'posts': posts
    }
    

    return HttpResponse(template.render(context, request))


def single(request, slug):

    post = Post.objects.get(slug=slug)

    content = f"<html><h1>{post.content}</h1></br><a href='{reverse('index')}'>home</a></html>"

    return HttpResponse(content)
