from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Category
from django.urls import reverse
from django.template import loader
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, CommentForm
from django.contrib.auth.models import User


class Index(ListView):
    model = Post
    template_name = "blog/posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def Single_post(request, slug):
    post = Post.objects.select_related('category', ).get(slug=slug)
    categories = Category.objects.all()
    form = CommentForm(request.POST)
    context = {
        'comment_form':form,
        'post': post,
        'category': post.category,
        'categories': categories,
        'comment': post.comment.filter(is_confirmed=True)
    }
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    else:
        context['form'] = form
    return render(request, "blog/post_single.html", context)


class Category_single(DetailView):
    model = Category
    template_name = 'blog/category_single.html'

    def get_context_data(self, **kwargs):
        category = Category.objects.get(slug=self.kwargs.get('slug'))
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug')
        context['posts'] = Post.objects.filter(category=category)
        context['categories'] = Category.objects.all()
        return context


def Login_form(request):
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


def Logout_form(request):
    logout(request)
    return redirect('index')


def Register_view(request):
    if request.method == 'POST':  # it will execute whene user submit form

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            return redirect('login')
        context = {'form': form}
    else:  # it will execute whene form will load
        form = UserRegistrationForm()
        context = {'form': form}

    return render(request, 'blog/register.html', context=context)
