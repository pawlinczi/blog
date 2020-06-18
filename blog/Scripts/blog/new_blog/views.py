from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'new_blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'new_blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']


def about(request):
    return render(request, 'new_blog/about.html', {'title': 'About'})
