from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Category
from django.urls import reverse
from django.template import loader
from django.views.generic import ListView , DetailView
# Create your views here.


# def index(request):
#     posts = Post.objects.all()

#     categories = Category.objects.all()

#     context = {
#         'posts': posts,
#         'categories': categories,
#     }

#     return render(request, "blog/posts.html", context)


class Index(ListView):
    model = Post
    template_name = "blog/posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['categories'] = Category.objects.all()
        return context


        

# def single(request, slug):

#     post = Post.objects.select_related('category',).get(slug=slug)
#     categories = Category.objects.all()
        

#     context = {
#         'post': post,
#         'category':post.category,
#         'categories': categories,
#         'comment': post.comment.filter(is_confirmed=True)
#     }

#     return render(request, "blog/post_single.html", context)

class Single(DetailView):
    model = Post
    template_name = "blog/post_single.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('comment')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['categories'] = Category.objects.all()
        return context
    

def category_single(request,slug):
    category = Category.objects.get(slug=slug)
    print(slug)
    cat_slug = Post.objects.filter(category=category)
    context={'cat_slug':cat_slug}
    return render(request, "blog/category_single.html", context)