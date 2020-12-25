from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Category
from django.urls import reverse
from django.template import loader
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm


class Index(ListView):
    model = Post
    template_name = "blog/posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def single(request, slug):
    post = Post.objects.select_related('category', ).get(slug=slug)
    categories = Category.objects.all()

    context = {
        'post': post,
        'category': post.category,
        'categories': categories,
        'comment': post.comment.filter(is_confirmed=True)
    }

    return render(request, "blog/post_single.html", context)


def category_single(request, slug):
    category = Category.objects.get(slug=slug)
    print(slug)
    cat_slug = Post.objects.filter(category=category)
    context = {'cat_slug': cat_slug}
    return render(request, "blog/category_single.html", context)


def login_form(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user_validation = authenticate(
            request, username=username, password=password)
        if user_validation and user_validation.is_active:
            login(request, user_validation)
            print(request.user)
            return redirect('index')
    elif request.method == "GET":
        pass

    return render(request, 'blog/login.html', context={})


def logout_form(request):
    logout(request)
    return redirect('index')


def register_view(request):
    if request.method == 'POST': # it will execute whene user submit form
        form = UserRegistrationForm(request.POST)
        context = {'form': form}
    else: # it will execute whene form will load
        form = UserRegistrationForm()
        context = {'form': form}

    return render(request, 'blog/register.html', context=context)
